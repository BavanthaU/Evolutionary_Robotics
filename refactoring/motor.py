import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        self.values = numpy.sin(numpy.linspace(-c.pi, c.pi, c.n)*self.frequency + self.offset)* self.amplitude
        numpy.save('data/'+jointName,self.values)
        
    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.values[t], maxForce = 80)

        
        

  

        

