#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = "870 Valencia St, San Francisco, CA 94110"

baseURL = "https://www.google.com/maps/"

webbrowser.open(baseURL + "place/" + address)
