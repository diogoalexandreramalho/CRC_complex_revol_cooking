import copy
import math
from Player import Player
from random import randrange

def loadPopulation(size):
	population = []
	for i in range(size):
		population.append(Player(i))
	return population

def makeProposal(total, part, responder):
	if part < responder.prfTrs:
		return False
	else:
		return True

def ultimatumIteration(population):
	responders = copy.deepcopy(population)
	proposers = []
	for i in range(math.floor(len(population) / 2)):
		proposers.append(responders.pop(randrange(len(responders))))

	#Reset Population
	population = []
	for proposer in proposers:
		target = responders.pop(randrange(len(responders)))

		#TODO: Different Slices
		accepted = makeProposal(proposer.amount, proposer.prfSlc, target)
		if accepted:
			target.amount += proposer.amount * proposer.prfSlc
			proposer.amount *= (1 - proposer.prfSlc)
			print("Responder", target.id, "accepted proposal of", proposer.id)
		else:
			proposer.amount = 0
			print("Responder", target.id, "refused proposal of", proposer.id)
		population.append(proposer)
		population.append(target)
	return population

def main():
	population = loadPopulation(10)
	population = ultimatumIteration(population)

main()
