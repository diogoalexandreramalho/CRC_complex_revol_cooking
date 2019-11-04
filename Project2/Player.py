import numpy as np
import random

class Player:
	def __init__(self, identifier):
		self.amount = 100
		self.prfTrs = random.randrange(0, 90, 1) / 100
		self.prfSlc = random.randrange(0, 90, 1) / 100
		self.tolerance = np.random.normal(0.5, 0.15)
		self.playHistory = []
		self.id = identifier
