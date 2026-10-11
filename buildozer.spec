[app]

title = Cyberpunk AI Core
package.name = cyberpunkai
package.domain = org.cyber
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3
source.include_dirs = assets
source.exclude_exts = spec
version = 1.0.0
requirements = python3,kivy,android,certifi,urllib3,requests,aiohttp,pyjnius,pillow,numpy
orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,VIBRATE,WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.package.format = apk

[buildozer]
log_level = 2
bin_dir = bin
warn_on_root = 1
