#!/usr/bin/env python

import sys
while True:
    line=raw_input()
    print ''.join([line.strip() for num in range(10)])
    sys.stdout.flush()
