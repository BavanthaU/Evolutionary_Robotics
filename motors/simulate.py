import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

amplitudeFront = numpy.pi/4.0
frequencyFront = 10
phaseOffsetFront = 0

amplitudeBack = numpy.pi/4.0
frequencyBack = 10
phaseOffsetBack = numpy.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
print("Value = " , robot)
p.loadSDF("world.sdf")
p.setGravity(0,0,-9.8)
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)
pyrosim.Prepare_To_Simulate("body.urdf")
targetAnglesFront = numpy.sin(numpy.linspace(-numpy.pi, numpy.pi, 1000)*frequencyFront + phaseOffsetFront)* amplitudeFront
targetAnglesBack = numpy.sin(numpy.linspace(-numpy.pi, numpy.pi, 1000)*frequencyBack + phaseOffsetBack)* amplitudeBack

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Back_Leg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBack[i], maxForce = 80)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Front_Leg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFront[i], maxForce = 80)
    time.sleep(.004)


p.disconnect()
numpy.save('data/backLegSensorValue',backLegSensorValues)
numpy.save('data/frontLegSensorValue',frontLegSensorValues)
numpy.save('data/targetAnglesFront',targetAnglesFront)
numpy.save('data/targetAnglesBack',targetAnglesBack)
