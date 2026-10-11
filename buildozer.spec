[app]

# (str) Title of your application
title = Supreme AI Core

# (str) Package name
package.name = supremeaicore

# (str) Package domain (needed for android packaging)
package.domain = org.supreme.ai

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# explicitly light requirements to ensure smooth cloud compilation
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether the application is an Android Service
android.service = True
