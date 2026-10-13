[app]

# (str) Title of your application
title = Cyberpunk AI System

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyber.ai

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Here we use the advanced/master branch version of Kivy directly from GitHub
requirements = python3,https://github.com/kivy/kivy/archive/master.zip,android,jnius

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = 

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (in hex format)
#android.presplash_color = #000000

# (string) Adaptive icon background (color #RRGGBB or image path)
#android.adaptive_icon_background = #000000

# (list) List of Java files to add to the android project (can be .java or .jar)
#android.add_java_files =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) The Android arch to build for, can be armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) Target API, should be as high as possible.
android.target_sdk = 33

# (int) Minimum API your APK will support.
android.min_sdk = 21

# (bool) Use asurface view for Kivy window
#android.surfaceview = False

# (str) Python for android (p4a) git branch to use
p4a.branch = master

# (str) OUYA Console support
#ouya.console.icon = data/icon/png.png

# (list) Icon of your application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Presplash of your application
#presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, storage for the android sdk/ndk
bin_dir = ./bin

# (bool) Skip to download the sdk/ndk (should be False if you are using CI)
skip_update = False
