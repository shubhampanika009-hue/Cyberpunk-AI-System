[app]

# (str) Title of your application
title = Cyberpunk AI System

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyber

# (str) Source files where the .py files are located
source.dir = .

# (list) Source files to include (let it include python files, images, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Added advanced libraries for robust performance
requirements = python3,kivy,plyer,certifi

# (list) Permissions required for background execution, audio, and storage
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,FOREGROUND_SERVICE

# (str) Supported orientations (portrait or landscape)
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 30

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
