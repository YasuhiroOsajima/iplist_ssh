#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys


org_file = sys.argv[1]
after_file = sys.argv[2]

cmd = "cat {} | col -bx > {}".format(org_file, after_file)
subprocess.call(cmd, shell=True)

