#Filter on file extensions

class Filters():

	def __init__(self):
		self._filters = []

	def set_filters(self, a_filters):
		try:
			self._filters = a_filters
		except:
			print("[ERROR] Can't apply filter rules")

	def get_filters(self):
		try:
			return self._filters
		except:
			print("[ERROR] Can't get filter rules")