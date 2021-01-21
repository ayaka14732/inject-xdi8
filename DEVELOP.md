# Packaging Guide

Every push commit to GitHub triggers a build action. An artifact `inject-xdi8.zip` will be generated on a successful build. This archive is for the Firefox version of this extension. To make it work on Chrome, you must manually substitute the string `moz-extension://` to `chrome-extension://` in `content_scripts/main.css`, and then re-generate the archive.
