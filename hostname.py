import sys
import os

#NETWORK TEST

class Test_hostname():

	def __init__(self):
		self._hostname = ""

	def set_hostname(self, hname):
		try:
			self._hostname = hname
			if self._hostname == '':
				self._hostname = 'google.com'
		except:
			print("[ERROR] Unable to set test hostname.")

	def get_hostname(self):
		try:
			return self._hostname
		except:
			print("[ERROR] Unable to get test hostname.")

	def test_conn(self):
		try:
			self._response = os.system("ping -c 1 " + self._hostname + " > /dev/null")

			if self._response == 0:
				print("The host [", self._hostname, "] answer. Connection OK.")
			else:
				print("[ERROR] The host [", self._hostname, "] doesn't answer. Check your connection.")
				sys.exit()
		except OSError:
			print("[ERROR] Unable to test network interface")
			sys.exit()