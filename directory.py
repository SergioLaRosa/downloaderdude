import os

#Directory for download

class Download_dir():

	def __init__(self):
		self._directory = ""

	def set_directory(self, a_dir):
		try:
			self._directory = a_dir
			#if the directory is empty in config.ini, set the default directory.
			if self._directory == '':
				self._directory = 'dd_files'
		except:
			print("[ERROR] Unable to set download dir name.")

	def get_directory(self):
		try:
			#if the directory is empty in config.ini, set the default directory.
			if self._directory=='':
				self._directory='dd_files'

			self._directory = os.path.abspath(self._directory)

			if os.path.isdir(self._directory) == False:
				os.mkdir(self._directory)
			return self._directory
		except:
			print("[ERROR] Unable to get download dir name.")