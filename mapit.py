#!/usr/bin/env python3

import sys
import webbrowser
import pyperclip

def main():
    """
    Opens the google map of the given address.
    """
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)

main()