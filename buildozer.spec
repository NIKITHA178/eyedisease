[app]
title = Eye Disease Classification
package.name = eyediseaseclassification
package.domain = org.myname
source.dir = .
version = 0.1
entrypoint = main.py
requirements = python3, kivy, opencv-python-headless, cvzone, pillow, numpy
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.minapi = 21
android.targetapi = 31
android.ndk = 25b
package.format = kivy
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png
fullscreen = 1
presplash.color = #ffffff
android.additional_build_options = --release
log_level = 2

[buildozer]
use_build_cache = True
