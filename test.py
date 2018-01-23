#!/usr/bin/env python3

import sys

try:
    import webbrowser
except ImportError as e:
    sys.exit(e.msg)

for url in sys.argv[1:]:
    try:
        webbrowser.open('https://' + url)
    except:
        pass

