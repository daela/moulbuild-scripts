#!/usr/bin/env python

import installer

files = [
"dirtsand.ini",
"static_ages.ini",
"bin/dirtsand"
]

installer.install("/home/branan/plasma/dirtsand/", "srv", files)