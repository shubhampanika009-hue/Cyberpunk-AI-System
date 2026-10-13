[app]

title = Cyberpunk AI
package.name = cyberpunkai
package.domain = org.cyberpunk.ai

source.include_exts = py,png,jpg,kv,atlas,html,js,css
source.include_patterns = *.html,assets/*

version = 0.5

requirements = python3,https://github.com/kivy/kivy/archive/master.zip,android,jnius

android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.cleartext_traffic = True

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
