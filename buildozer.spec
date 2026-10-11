[app]

# (str) Title of your application
title = Cyberpunk AI Core

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyber

# (str) Source code directory where main.py lives (CRITICAL FIX)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3

# (list) List of directory to include
source.include_dirs = assets

# (list) Source files to exclude
source.exclude_exts = spec

# (str) Application versioning
version = 1.0.0

# (list) Application requirements (Advanced AI, Networking, Audio, and Kivy Dependencies)
requirements = python3,kivy,android,certifi,urllib3,requests,aiohttp,pyjnius,pillow,numpy,chardet,idna

# (str) Supported orientations
orientation = portrait

# (list) Advanced Android Permissions for Full Cyberpunk AI Operations
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,VIBRATE,WAKE_LOCK

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android architectures to build for (Supports 64-bit & 32-bit devices)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable/disable confirmation to allow application to run in background
android.allow_backup = True

# (str) Format used to package the app
android.package.format = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact
bin_dir = bin

# (int) Display warning about building as root
warn_on_root = 1
