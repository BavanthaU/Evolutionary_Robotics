import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self,id):
        self.myID = id
        self.weightsSensorToHidden =  2*numpy.random.rand(c.numSensorNeurons,c.numHiddenNeurons)-1
        self.weightsHiddenToMotor = 2*numpy.random.rand(c.numHiddenNeurons,c.numMotorNeurons)-1


    def Start_Simulation(self,mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py {0} {1} &".format(mode, str(self.myID)))

    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName)
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness{0}.txt".format(str(self.myID)))
        os.system("rm body{0}.urdf".format(str(self.myID)))
        os.system("rm world{0}.sdf".format(str(self.myID)))



    def Create_World(self):
        pyrosim.Start_SDF("world"+str(self.myID)+".sdf")
        for row in range(5):
            for column in range(5):
                pyrosim.Send_Cube(name="Box", pos=[row*-4-4,column*-5+8,1] , size=[1,1,2], mass=20.0)
        pyrosim.End() 

    def Create_Body(self):
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -.5 1",jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5, 0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 .5 1",jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LefttLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-.5 0 1",jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = ".5 0 1",jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0] , size=[1, 0.2,0.2])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = "0 1 0",jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[0.2, 0.2,1])

        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = "0 -1 0",jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[0.2, 0.2,1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = "-1 0 0",jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5] , size=[0.2, 0.2,1])

        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = "1 0 0",jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[0.2, 0.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LefttLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")

        for n in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron( name =c.numMotorNeurons+c.numSensorNeurons+n)

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons+c.numMotorNeurons , weight = self.weightsSensorToHidden[currentRow][currentColumn])
        
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow+c.numSensorNeurons+c.numMotorNeurons, targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weightsHiddenToMotor[currentRow][currentColumn])
        pyrosim.End()

    
    def Mutate(self):
        self.weightsSensorToHidden[random.randint(0,c.numSensorNeurons-1),random.randint(0,c.numHiddenNeurons-1)] = random.random()*2-1
        self.weightsHiddenToMotor[random.randint(0,c.numHiddenNeurons-1),random.randint(0,c.numMotorNeurons-1)] = random.random()*2-1
        

    
    def Set_ID(self, id):
        self.myID = id
    
    def Start_Best_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py {0} {1}".format("GUI", str(self.myID)))
                