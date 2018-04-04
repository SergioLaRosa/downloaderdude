#URLs processed simultaneously

class Batch():

	def __init__(self):
		self._batch = 0

	def set_batch(self, n_batch):
		try:
			self._batch = n_batch
		except:
			print("[ERROR] Can't set task batch number.")

	def get_batch(self):
		try:
			return self._batch
		except:
			print("[ERROR] Can't get task batch number.")