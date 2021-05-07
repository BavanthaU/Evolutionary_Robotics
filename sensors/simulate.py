import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
p.setGravity(0,0,-9.8)
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)
pyrosim.Prepare_To_Simulate("body.urdf")

for i in range(50):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(backLegSensorValues[i], " : ",frontLegSensorValues[i])
    time.sleep(.1)


p.disconnect()
print(backLegSensorValues)
numpy.save('data/backLegSensorValue',backLegSensorValues)
numpy.save('data/frontLegSensorValue',frontLegSensorValues)
