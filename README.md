# Sadhana

A devotional app for my phone with mantras, japa counting, festivals and a calendar. It is one HTML file that works offline, and Capacitor wraps it for Android.

- `sadhana-android/www/index.html` is the app
- `sadhana-android/` is the Capacitor project
- `.github/workflows/android.yml` builds the APK

## Install

Download `Sadhana.apk` from the [latest release](https://github.com/AbhishekSrinivas/Sadhana-App/releases/latest), open it on an Android phone and allow installs from your browser or file manager when asked. Every push to `main` rebuilds the APK and replaces the release. The APK is debug-signed, so installing a new one over the old one keeps your data.


## Updates without a new APK

The installed app looks at the latest release for `version.json` when it opens (after a few seconds) and when you tap Check for updates in the menu. If the build number is newer, it downloads `app.html`, keeps it on the device and shows an Update ready bar. Restart applies it. Your saved mantras, counts and settings are not touched. If an update fails to start, the app removes it and falls back to the version inside the APK.

- Needs internet and a public repository.
- Install the APK once from this build. After that, each push to `main` can be pulled in from the app.
- Native changes (new plugins, permissions, icon) still need a new APK.

## Build the APK yourself

Run **Build Sadhana APK** from the Actions tab and download the artifact, or build locally.

With Android Studio: `cd sadhana-android && npm install && npx cap sync android && npx cap open android`.

To ship a new version, replace `www/index.html`, run `npx cap sync android` and rebuild.

The astronomy calculations use Astronomy Engine by Don Cross (MIT), included in `index.html` with its notice.
