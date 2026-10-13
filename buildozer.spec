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
version = 0.3

# (list) Application requirements
# Add python, kivy, jnius and webview dependencies here
requirements = python3,kivy,android,jnius

# (str) Custom source folders for python modules
#source.dirs = .

# (list) Permissions
# Added INTERNET, RECORD_AUDIO, and MODIFY_AUDIO_SETTINGS for WebView and Voice Agent
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS

# (str) Supported orientations (landscape or portrait)
orientation = portrait

# (list) List of service to declare
#services = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
