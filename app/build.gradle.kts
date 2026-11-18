plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

android {
    namespace = "com.gandalondon.stepback"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.gandalondon.stepback"
        minSdk = 29
        targetSdk = 35
        versionCode = (System.getenv("GITHUB_RUN_NUMBER") ?: "1").toInt()
        versionName = "0.1.${System.getenv("GITHUB_RUN_NUMBER") ?: "0"}"
    }

    // Signing key comes from CI secrets (never committed). Same key on every
    // build means updates install over the top and keep what Stepback found.
    val ks = System.getenv("SIGNING_KEYSTORE_PATH")
    signingConfigs {
        create("personal") {
            if (ks != null) {
                storeFile = file(ks)
                storePassword = System.getenv("SIGNING_PASSWORD")
                keyAlias = "stepback"
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
    buildFeatures { compose = true }
}

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
