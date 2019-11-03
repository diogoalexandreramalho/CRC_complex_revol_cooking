import numpy as np

class Player:
	def __init__(self, identifier):
		self.amount = 100
		self.prfTrs = 0.1
		self.tolerance = np.random.normal(0.5, 0.15)
		self.playHistory = []
		self.id = identifier
