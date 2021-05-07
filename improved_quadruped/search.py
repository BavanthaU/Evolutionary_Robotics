import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pickle

phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()
# phc.Show_Best()


bestRobots = open("bestRobotGen1.p", "rb")
loaded_dictionary = pickle.load(bestRobots)
print(loaded_dictionary)
phc.Simulate_Best(loaded_dictionary)
