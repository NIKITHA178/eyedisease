[app]
# (str) Title of your application
title = Eye Disease Classification

# (str) Package name
package.name = eyediseaseclassification

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = model/*, images/*

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy
requirements = python3,kivy,opencv-python-headless,cvzone

# (str) Presplash screen used for loading. Default is None (no presplash).
#presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/images/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, used by Buildozer (min API level 21)
android.api = 30

# (int) Android NDK version to use (default is 21b)
android.ndk = 21b

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Packaging domain for Android/iOS
package.domain = org.example

# (bool) Enable the usage of Android's blacklist functionality
android.blacklist_remove_default = False

# (bool) Indicate if the application should be a window or not (on platforms that support this)
#window = 1

# (str) Path to the file where the log will be written
#log.filename = %(source.dir)s/application.log

# (list) Source files to be included in the final package
source.include_patterns = model/*

# (list) Source files to be excluded from the final package
source.exclude_exts = spec

# (bool) Enable presplash screen
#presplash.enabled = False

# (str) Presplash screen used for loading. Default is None (no presplash).
#presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/images/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, used by Buildozer (min API level 21)
android.api = 30

# (int) Android NDK version to use (default is 21b)
android.ndk = 21b

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Packaging domain for Android/iOS
package.domain = org.example

# (bool) Enable the usage of Android's blacklist functionality
android.blacklist_remove_default = False

# (bool) Indicate if the application should be a window or not (on platforms that support this)
#window = 1

# (str) Path to the file where the log will be written
#log.filename = %(source.dir)s/application.log

# (list) Source files to be included in the final package
source.include_patterns = model/*

# (list) Source files to be excluded from the final package
source.exclude_exts = spec

# (bool) Enable presplash screen
#presplash.enabled = False

# (str) Presplash screen used for loading. Default is None (no presplash).
#presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/images/icon.png
