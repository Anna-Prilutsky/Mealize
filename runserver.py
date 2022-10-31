#!/usr/bin/env python

#-----------------------------------------------------------------------
# runserver.py
# Author: Shameek Hargrave
# Purpose: Runs a Flask test server on specified port to serve a web
# application for regristar database information.
#-----------------------------------------------------------------------

import sys
import argparse
import generate_plan as gen_plan


#-----------------------------------------------------------------------

def main():
    # Open a socket and accept all connection requests
    try:
        gen_plan.app.run(host='0.0.0.0', port="5000")

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(2)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()