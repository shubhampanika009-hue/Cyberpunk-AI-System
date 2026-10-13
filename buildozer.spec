[app]

# (str) Title of your application
title = Cyberpunk AI

# (str) Package name
package.name = cyberpunkai

# (str) Package domain (needed for android packaging)
package.domain = org.cyberpunk.ai

# (list) Source files to include (let it include all Python and web assets)
source.include_exts = py,png,jpg,kv,atlas,html,js,css

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,*.html

# (str) Application versioning
version = 0.4

# (list) Application requirements (Kivy का एडवांस मास्टर वर्जन शामिल है)
requirements = python3,https://github.com/kivy/kivy/archive/master.zip,android,jnius

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (bool) Indicate whether the application can use cleartext traffic (HTTP)
android.cleartext_traffic = True

# (str) Supported orientations (landscape or portrait)
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
