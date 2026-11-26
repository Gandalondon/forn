plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

val store = project.hasProperty("store")

android {
    namespace = "com.gandalondon.stepback"
    compileSdk = 36

    defaultConfig {
        // Play Store id (24 Nov, matches app.getsniff, app.getarcrelay, app.gethlid). Only the store build uses it (-Pstore),
        // so Tony's Obtainium install (com.gandalondon.stepback) keeps its rings and keeps updating. The code's namespace stays.
        applicationId = if (store) "app.getforn" else "com.gandalondon.stepback"
        minSdk = 29
        targetSdk = 36 // Play needs API 36 (26 Nov)
        // Version naming, same in every app (Tony, Nov 2026): the version is set by hand (1.0 at launch, 1.0.1 for
        // fixes, 1.1 for features), the build is the GitHub run number. Shown as Version 1.0 (115).
        versionCode = (System.getenv("GITHUB_RUN_NUMBER") ?: "1").toInt()
        versionName = "1.0"
        // The Play build (-Pstore, 26 Nov) has no test tools: no Send my data, Record walk, Show six months,
        // test log or crash page, and only the London set of facts (no Scotland).
        buildConfigField("boolean", "STORE", if (store) "true" else "false")
    }

    // Signing key comes from CI secrets (never committed). Same key on every
    // build means updates install over the top and keep what Forn found.
    val ks = System.getenv("SIGNING_KEYSTORE_PATH")?.takeIf { it.isNotBlank() }
    signingConfigs {
        create("personal") {
            if (ks != null) {
                storeFile = file(ks)
                storePassword = System.getenv("SIGNING_PASSWORD")
                keyAlias = System.getenv("SIGNING_KEY_ALIAS") ?: "stepback" // the Play upload key is "forn"
                keyPassword = System.getenv("SIGNING_PASSWORD")
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            signingConfig = if (ks != null) signingConfigs.getByName("personal")
            else signingConfigs.getByName("debug")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
    buildFeatures { compose = true; buildConfig = true }

    // Store build only: a manifest without the Record walk service and its foreground location permissions,
    // and a London-only spots.json that overrides the main one.
    if (store) {
        sourceSets.getByName("release") {
            manifest.srcFile("src/store/AndroidManifest.xml")
            assets.srcDir(layout.buildDirectory.dir("storeAssets"))
        }
    }
}

// London only for Play: leaves out the Scotland facts (Aberdeen and Portlethen, Tony's trips).
val storeSpots by tasks.registering {
    val src = file("src/main/assets/spots.json")
    val out = layout.buildDirectory.file("storeAssets/spots.json")
    inputs.file(src); outputs.file(out)
    doLast {
        @Suppress("UNCHECKED_CAST")
        val all = groovy.json.JsonSlurper().parse(src) as List<Map<String, Any>>
        val kept = all.filter { s -> (s["points"] as List<List<Number>>).all { it[0].toDouble() < 54.0 } }
        out.get().asFile.apply { parentFile.mkdirs(); writeText(groovy.json.JsonOutput.toJson(kept)) }
        println("Store spots: ${kept.size} of ${all.size}")
    }
}
if (store) tasks.matching { it.name.startsWith("merge") && it.name.endsWith("Assets") }.configureEach { dependsOn(storeSpots) }

dependencies {
    val composeBom = platform("androidx.compose:compose-bom:2024.12.01")
    implementation(composeBom)
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.foundation:foundation")
    implementation("androidx.compose.material3:material3")

    implementation("androidx.core:core-ktx:1.15.0")
    implementation("androidx.activity:activity-compose:1.9.3")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.8.7")

    // Geofencing. Nothing leaves the phone: no network permission at all.
    implementation("com.google.android.gms:play-services-location:21.3.0")
    // Play services pulls in an old Fragment; the permission prompts need 1.3+.
    implementation("androidx.fragment:fragment-ktx:1.8.5")
}
