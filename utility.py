import threading
import sys
import os
from datetime import datetime

# Logger


class Logger():

    def __init__(self):
        self._file = ""

    def set_file(self, logname):
        self._file = logname

    def get_file(self):
        return self._file

    def logger(self, event):
        try:
            with open(self._file, 'a') as self._fp:
                self._fp.write(event)
        except BaseException:
            print("[ERROR] Unable to provide logging.")


# Test connection
class Check_conn():

    def __init__(self):
        self._test_hostname = ""

    def set_test_hostname(self, hostname):
        self._test_hostname = hostname

    def get_test_hostname(self):
        return self._test_hostname

    def test_conn(self):
        try:
            self._response = os.system(
                "ping -c 1 " + self._test_hostname + " > /dev/null")

            if self._response == 0:
                print(
                    "The host [",
                    self._test_hostname,
                    "] answer. Connection OK.")
            else:
                print("[ERROR] The host [", self._test_hostname,
                      "] doesn't answer. Check your connection.")
                sys.exit()
        except OSError:
            print("[ERROR] Unable to test network interface")
            sys.exit()

# Filtering URLs


class Filtered_urls():

    def __init__(self):
        self._checked = []

    def apply_filters(self, filters, sources):
        try:
            self._filters = filters
            self._sources = sources

            for self._i, self._val in enumerate(self._sources):

                if not self._filters:
                    self._checked = self._sources

                # for .<xyz> extensions
                if self._val[-4:] in self._filters:
                    self._checked.append(self._val)

                # for .<qxyz> extensions
                if self._val[-5:] in self._filters:
                    self._checked.append(self._val)

                # for .<qwx>.<yz> extensions
                if self._val[-7:] in self._filters:
                    self._checked.append(self._val)
            return self._checked

        except BaseException:
            print("[ERROR] Unable to apply filters.")
