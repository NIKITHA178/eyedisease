[app]

# (str) Title of your application
title = Eye Disease Classification

# (str) Package name
package.name = eyediseaseclassification

# (str) Package domain (e.g. org.myname.myapp)
package.domain = org.myname

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (e.g. 1.0.0)
version = 0.1

# (str) Application entry point
entrypoint = main.py

# (list) Application requirements (comma separated)
# Ensure all dependencies are listed here
requirements = python3, kivy, opencv-python-headless, cvzone, pillow, numpy

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (str) Supported Android SDK version
android.minapi = 21
android.targetapi = 30
android.ndk = 21b

# (str) The format used to package the application
# Acceptable formats: kivy, pygame
package.format = kivy

# (str) Presplash screen
# An image file for presplash screen
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# Path to an image file for the icon
icon.filename = %(source.dir)s/data/icon.png

# (bool) Indicate if the application is fullscreen
fullscreen = 1

# (str) Presplash background color (default is black)
presplash.color = #ffffff

# (list) Additional build options
android.additional_build_options = --release

# (str) Path to custom keystore for signing
# Uncomment and set these if you have a keystore for signing
# android.keystore = path/to/keystore
# android.keystore_pass = password
# android.key_alias = alias
# android.key_alias_pass = alias_password

# (bool) Indicate if the application is a service
android.service = False

# (str) The directory where the compiled .apk file will be stored
# The default is the dist/ directory
build_dir = build

# (str) Custom build configuration
# android.custom_build = src/custom_build

# (str) Extra files to include in the package
# android.extra_files = src/extra_files

# (list) Android build options
android.build_options = --release

# (bool) Enable the debug log
log_level = 2

[buildozer]

# (bool) Use the build cache
use_build_cache = True
