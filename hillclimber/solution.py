import numpy
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:
    def __init__(self):
        self.weights =  2*numpy.random.rand(3,2)-1
        print(self.weights)
    
    def Evaluate(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py {0}".format(mode))
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0,5,0.5] , size=[1,1,1])
        pyrosim.End() 

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        sensors=[0,1,2]
        motors=[3,4]
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(len(sensors)):
            for currentColumn in range(len(motors)):
                pyrosim.Send_Synapse( sourceNeuronName = sensors[currentRow], targetNeuronName = motors[currentColumn] , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    
    def Mutate(self):
        self.weights[random.randint(0,2),random.randint(0,1)] = random.random()*2-1
                