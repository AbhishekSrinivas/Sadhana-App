# Sadhana

A devotional app for my phone: mantras, japa counting, festivals and a calendar. It is one HTML file that works offline, wrapped for Android with Capacitor.

- `sadhana-android/www/index.html` is the app
- `sadhana-android/` is the Capacitor project
- `.github/workflows/android.yml` builds the APK

## Build the APK

Run **Build Sadhana APK** from the Actions tab, wait about five minutes, download the artifact and unzip it to get `app-debug.apk`. Copy it to the phone and allow installs from that source.

With Android Studio: `cd sadhana-android && npm install && npx cap sync android && npx cap open android`.

To ship a new version, replace `www/index.html`, run `npx cap sync android` and rebuild.

The astronomy calculations use Astronomy Engine by Don Cross (MIT), included in `index.html` with its notice.
