import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, sensorName):
        self.linkname = sensorName
        self.values = numpy.zeros(c.n)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        if(t == c.n-1):
            numpy.save('data/'+self.linkname,self.values)
    