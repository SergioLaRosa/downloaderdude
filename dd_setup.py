import os
import configparser
import threading
import sys
from datetime import datetime
try:
    import hostname
    import sources
    import filters
    import directory
    import utility
    import batch
except ImportError:
    print("[ERROR] Unable to find script modules.")
    sys.exit()


# Script setup

class Settings():

    def __init__(self):
        self._config = configparser.ConfigParser()

    def setup(self):
        # CONFIG PARAMETERS
        try:
            with open('config.ini') as self._cfg:
                self._config.read_file(self._cfg)
                self._hname = self._config.get("TestHost", "hostname")
                self._dd_dir = self._config.get("Dir", "dd_dir")
                self._src = self._config.get("Sources", "sources")
                self._a_filters = (
                    self._config.get(
                        "Filters",
                        "filters")).split(', ')
                self._n_batch = self._config.get("Batch", "n_batch")
                if self._n_batch:
                    self._n_batch = int(self._n_batch)

            print("\n[NOTICE] Check your settings in 'config.ini' file. ")

        except (IOError, OSError):
            print("[ERROR] Unable to find config file (config.ini)")
            sys.exit()

        # NETWORK TEST
        try:
            print("\n>>Test network connection...")
            self._hostname = hostname.Test_hostname()
            self._hostname.set_hostname(self._hname)
            self._hostname.get_hostname()
            self._hostname.test_conn()

        except (IOError, OSError):
            print("[ERROR] Unable to get test_hostname.")

        # Logging...
        self._setup_log = utility.Logger()
        self._setup_log.set_file('log.txt')
        self._setup_log.get_file()

        # BEGIN SETUP
        #########################
        try:
            # DIRECTORY
            self._dd_directory = directory.Download_dir()
            self._dd_directory.set_directory(self._dd_dir)
            self._dd_directory = self._dd_directory.get_directory()

            # BATCH FOR TASK POOL
            self._batch = batch.Batch()
            self._batch.set_batch(self._n_batch)
            self._batch = self._batch.get_batch()

            # FILTERS
            self._filters = filters.Filters()
            self._filters.set_filters(self._a_filters)
            self._filters = self._filters.get_filters()

            # SOURCES
            # There is no need to set a default action. If the source file doesn't exist or it's corrupted,
            # the script will terminate its operation instantly.
            print("\n>>Source File:")
            print(self._src)
            self._sources = sources.Sources()
            self._sources.set_urls(self._src)
            self._sources = self._sources.get_urls()

            print("\n>>Options")
            print("Download directory: ", self._dd_dir)

            # If filters is empty in config.ini, don't apply filters.
            if self._a_filters[0] == '' and len(self._a_filters) == 1:
                self._filtered_urls = self._sources
                print("No filter rules applied.\n")
            else:
                print("Filter rules: ", self._a_filters, "\n")
                self._filtered_urls = utility.Filtered_urls()
                self._filtered_urls = self._filtered_urls.apply_filters(
                    self._a_filters, self._sources)

            # for logging...
            self._conf_log = "\n[CONFIG] [time: " + str(
                (datetime.now()).strftime('%Y/%m/%d %H:%M:%S')) + "] Setup complete. [OK]"
            self._setup_log.logger(self._conf_log)

        except BaseException:
            print("[ERROR] Unable to complete script setup.")
            self._fail_conf_log = "\n[ERROR] [time: " + str(
                (datetime.now()).strftime('%Y/%m/%d %H:%M:%S')) + "] Setup Failed!!!"
            self._setup_log.logger(self._fail_conf_log)
            sys.exit()

        return self._filtered_urls, self._dd_directory, self._n_batch
