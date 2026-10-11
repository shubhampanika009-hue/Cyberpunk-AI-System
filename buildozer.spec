[app]

# (str) Title of your application
title = Cyberpunk AI System

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyber

# (str) Source files where the .py files are located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,plyer,certifi

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,FOREGROUND_SERVICE

# (str) Supported orientations
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 30

fullscreen = 0

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
