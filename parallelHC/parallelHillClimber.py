from solution import SOLUTION
import copy
import constants as c
import os
import pickle

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parent ={}
        self.nextAvailableID=0
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        for i in range(c.populationSize):
            self.parent[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parent)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        
    
    def Spawn(self):
        self.children = {}
        for p in self.parent:
            self.children[p] = copy.deepcopy(self.parent[p])
            SOLUTION.Set_ID(self.children[p],self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for c in self.children:
            self.children[c].Mutate()

    def Select(self):
        for i in self.parent:
            if (self.parent[i].fitness > self.children[i].fitness):
                self.parent[i] = self.children[i]
        
    def Print(self):
        print("")
        for i in self.parent:
            print(i,"P: ",self.parent[i].fitness, "C: " ,self.children[i].fitness)
        print("")
    

    def Evaluate(self,solutions):
        for p in solutions:
            SOLUTION.Start_Simulation(solutions[p],"DIRECT")
        for p in solutions:
            SOLUTION.Wait_For_Simulation_To_End(solutions[p])
    
    def Show_Best(self):
        for p in self.parent:
            SOLUTION.Start_Simulation(self.parent[p],"GUI")
        # f = open('bestRobot.p', 'wb')
        # pickle.dump(self.parent, f)
        # f.close()
    
    def Simulate_Best(self, solutions):
        for p in solutions:
            SOLUTION.Start_Simulation(solutions[p], "GUI")

