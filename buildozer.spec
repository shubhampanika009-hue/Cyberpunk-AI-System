[app]

# (str) Title of your application
title = Cyberpunk AI Core

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyber

# (list) Source files to include (let it include python files, assets, etc.)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of directory to include (optional)
source.include_dirs = assets

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusions using pattern matching
source.exclude_patterns = license,images/*.jpg

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Add all python libraries required for your cyberpunk AI core & Kivy
requirements = python3,kivy,android,certifi,urllib3,requests,aiohttp,pyjnius

# (list) Custom source folders for python modules
# source.pie_path = 

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS

# (list) features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use (Left blank to let buildozer auto-manage safely without warnings)
# android.sdk = 

# (str) Android arch to build for, choose targets
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable/disable confirmation to allow application to run in background
android.allow_backup = True

# (str) Fullname to use for entering in the keystore
#android.fullname = 

# (str) The format used to package the app for release/debug
android.package.format = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact
bin_dir = bin

# (int) Display warning about building as root
warn_on_root = 1
