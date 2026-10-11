[app]

# (str) Title of your application
title = Supreme AI Core

# (str) Package name
package.name = supremeaicore

# (str) Package domain (needed for android packaging)
package.domain = org.supreme.ai

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Directory where the source files are located
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use ( dejamos blank for automatic installation )
# android.sdk = 33

# (str) Android entry point
# android.entrypoint = org.renpy.android.PythonActivity

# (list) The gservices.json file (optional)
# android.gservices_path = 

# (bool) Indicate whether the application is an Android Service or not
android.service = True

# (str) Application versioning
version = 0.1

# (list) Custom XML attributes to add to AndroidManifest.xml
# android.manifest.xml_extra = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
