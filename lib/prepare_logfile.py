# -*- coding: utf-8 -*-
"""
Prepare logfile for ssh command operation.
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import os
import re
import stat
import sys
from datetime import datetime


class PrepareLogfile(object):
    def __init__(self):
        self.logfile_dir = \
            os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')

    def _make_logfilepath(self, targethost):
        logfile_name = "{host}_{date}.log".format(
            host=targethost,
            date=datetime.now().strftime("%Y%m%d%H%M%S"))

        logfile_path = os.path.join(self.logfile_dir, logfile_name)
        return logfile_path

    def _create_logfile(self, logfile_path):
        if not os.path.isdir(self.logfile_dir):
            os.mkdir(self.logfile_dir)

        with open(logfile_path, 'w'):
            pass

        #os.chmod(logfile_path, stat.S_IEXEC)
        return os.path.isfile(logfile_path)

    @staticmethod
    def _make_hostname_safe(targethost):
        targethost = re.sub(re.compile("[!-,/:-@[-`{-~]"), '', targethost)
        targethost = re.sub(r' ', '', targethost)

        return targethost

    def prepare_logfile(self, targethost_input):
        "Create logfile in advance ssh connection."

        targethost = self._make_hostname_safe(targethost_input)
        logfile_path = self._make_logfilepath(targethost)
        if not self._create_logfile(logfile_path):
            print("Cloud not prepare log file. "
                  "Please check your filesystem.\n"
                  "logfile directory: {}".format(self.logfile_dir))
            sys.exit(2)

        return logfile_path
