#!/usr/bin/python3

import threading
import os
import glob
import sys
import time
from queue import Queue
from datetime import datetime
import argparse
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
try:
    import dd_setup
    import utility
except ImportError:
    print("[ERROR] Unable to find script modules.")
    sys.exit()


class Downloader(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue  # get the queue

    def run(self):
        while True:
            url = self.queue.get()  # url is provided as ext. parameter via download_file, check below
            self.download_file(url)  # download the current url
            self.queue.task_done()  # operation complete

    def download_file(self, url):

        # for log
        self._down_log = utility.Logger()
        self._down_log.set_file('log.txt')
        self._down_log.get_file()

        try:
            # test URL
            self._handle = urllib2.urlopen(url)
            self._fname = dd_directory + "/" + os.path.basename(url)
            print("[...] Downloading: ", url, " ... ")
            with open(self._fname, "wb") as self._f:
                while True:
                    self._chunk = self._handle.read(1024)
                    if not self._chunk:
                        break
                    self._f.write(self._chunk)
            print("[OK] ", url, "downloaded.")

            # report success
            self._ok_dd_log = "\n[OK] [time: " + str((datetime.now()).strftime(
                '%Y/%m/%d %H:%M:%S')) + "] url: " + url + " downloaded."
            self._down_log.logger(self._ok_dd_log)

        except (ValueError, OSError):
            # report errors
            print(
                "[ERROR]",
                url,
                "Unable to resolve URL and/or write file on disk.")
            self._fail_dd_log = "\n[ERROR] [time: " + str(
                (datetime.now()).strftime('%Y/%m/%d %H:%M:%S')) + "] Download failed for " + url
            self._down_log.logger(self._fail_dd_log)


def main(urls, n_urls):

    # for log
    main_log = utility.Logger()
    main_log.set_file('log.txt')
    main_log.get_file()

    try:
        print(">>Starting download...")

        # For benchmarks purpose...
        start_time = time.time()

        # Create the queue
        queue = Queue()

        # Create a thread pool and give them a queue
        for i in range(n_urls):
            t = Downloader(queue)
            t.setDaemon(True)  # daemon threads can be stopped anytime
            t.start()

        # Give the queue some data
        for url in urls:
            queue.put(url)

        # Wait for the queue to finish
        queue.join()

        print(
            "\n[NOTICE] Session completed in: %s seconds" %
            (time.time() - start_time))

    except KeyboardInterrupt:
        print("NOTICE] Script stopped during execution. (Ctrl+C)")
        exec_log = "\n[ERROR] [time: " + str((datetime.now()).strftime(
            '%Y/%m/%d %H:%M:%S')) + "] Script interrupted (Ctrl+C)!"
        main_log.logger(exec_log)


if __name__ == "__main__":

    print("Download Manager - beta_2")

    # Start Setup
    conf = dd_setup.Settings()
    settings = conf.setup()

    # Get the settings...
    urls = settings[0]
    dd_directory = settings[1]
    n_batch = settings[2]

    if not n_batch:
        # all the URLs, filtered or not
        n_urls = len(urls)
    else:
        # batch of n_urls for every iteration
        n_urls = n_batch

    try:
        main(urls, n_urls)
    except BaseException:
        print(
            "[NOTICE] Script stopped during execution and/or crashed. Try restarting it.")
