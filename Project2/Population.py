import copy
import math
from Player import Player
from Proposal import Proposal
from random import randrange

def loadPopulation(size):
	population = []
	for i in range(size):
		population.append(Player(i))
	return population

def ultimatumIteration(population):
	responders = copy.deepcopy(population)
	proposers = []
	for i in range(math.floor(len(population) / 2)):
		proposers.append(responders.pop(randrange(len(responders))))
	for proposer in proposers:
		target = responders.pop(randrange(len(responders)))
		print("Proposer", proposer.id, "targets", target.id)
		#TODO: make proposal
	#TODO:update each player's preferences (elements discuss with random neighbours)
	#TODO:update population

def main():
	population = loadPopulation(10)
	ultimatumIteration(population)

main()
