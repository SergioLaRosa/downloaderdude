import pickle

# URLs sources


class Sources():

    def __init__(self):
        self._text_file = ""
        self._urls = []

    def set_urls(self, fname):
        try:
            self._text_file = open(fname, "r")
            self._urls = self._text_file.read().split('\n')
        except IOError:
            print("[ERROR] Unable to read source URLs")
            print("[ERROR] Source file: [", fname, "] not found!!!.")

    def get_urls(self):
        try:
            return self._urls
        except IOError:
            print("[ERROR] Unable to get source URLs")
