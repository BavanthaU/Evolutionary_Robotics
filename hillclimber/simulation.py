import pybullet as p
import time
from world import WORLD
from robot import ROBOT
import constants as c
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self, mode):
        self.directOrGUI = mode
        if(self.directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        elif(self.directOrGUI=="GUI"):
            self.physicsClient = p.connect(p.GUI)

        self.world = WORLD()
        self.robot =  ROBOT()
     

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(c.n):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if(self.directOrGUI == "GUI"):
                time.sleep(c.numTimeSteps)
            
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()