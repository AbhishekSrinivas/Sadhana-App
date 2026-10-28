# Sadhana

A private, phone-first devotional companion app: mantras, japa counting, festivals and a calendar. It runs fully on the device as a single HTML page, wrapped for Android with Capacitor.

## Repository layout

| Path | Contents |
|---|---|
| `sadhana-android/www/index.html` | The app (single file, offline) |
| `sadhana-android/` | Capacitor project and Android wrapper |
| `.github/workflows/android.yml` | GitHub Actions workflow that builds the APK |

## Build the APK

1. Open the repository's **Actions** tab and run **Build Sadhana APK**.
2. Download the artifact when it finishes (about 5 minutes) and unzip it to get `app-debug.apk`.
3. Copy it to your phone and allow installs from this source.

With Android Studio instead: `cd sadhana-android && npm install && npx cap sync android && npx cap open android`.

## Updating the app

Replace `sadhana-android/www/index.html`, then run `npx cap sync android` and rebuild.

## Credits

Astronomy calculations use the MIT-licensed Astronomy Engine by Don Cross, bundled in `index.html` with its original notice.
