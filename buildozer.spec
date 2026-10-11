[app]

# (str) Application Title
title = Supreme AI Core

# (str) Package name
package.name = supremeaicore

# (str) Package domain (needed for android packaging)
package.domain = org.rajasingh

# (str) Source directory where the application files reside
source.dir = .

# (list) Source files to include (py, kv, png, jpg, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, venv, .git

# (str) Application versioning
version = 10.0.0

# (list) Application requirements
requirements = python3,kivy,pyjnius,android

# (list) Supported orientations
orientation = portrait

# (list) Complete Enterprise Android Permissions
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,VIBRATE,WAKE_LOCK,FOREGROUND_SERVICE

# (int) Target Android API (API 33 for modern Android compatibility)
android.api = 33

# (int) Minimum API supported by your APK
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto backup
android.backup = False

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (str) Path to build artifact storage
bin_dir = ./bin
