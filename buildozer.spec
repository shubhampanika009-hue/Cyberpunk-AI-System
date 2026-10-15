[app]

# (str) Title of your application
title = 5-Agent Neural Matrix

# (str) Package name
package.name = cyberpunkmatrix

# (str) Package domain (needed for android packaging)
package.domain = org.cyberpunk.matrix

# (list) Source files to include (let it include python files, kv, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of directory to include/exclude from source dir
source.include_dirs = 

# (list) Application requirements
requirements = python3,kivy,jnius

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether the application is an Andoird service or not
android.service = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if build on root (0 = False, 1 = True)
warn_on_root = 1
