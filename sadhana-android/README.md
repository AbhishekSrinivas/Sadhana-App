# Sadhana for Android

## Get the APK (no Android Studio needed)
1. Create a new private repository on GitHub and upload everything in this folder.
2. Open the repository, go to Actions, choose "Build Sadhana APK" and click Run workflow.
3. When it finishes (about 5 minutes), open the run and download the "Sadhana-APK" file. Unzip it to get app-debug.apk.
4. Copy the APK to the phone or tablet, open it and allow "install from this source". Done.

## With Android Studio instead
npm install, then npx cap sync android, then npx cap open android and press Run.

## Updating the app later
Replace www/index.html with the new version, then run npx cap sync android and rebuild.
