import pybullet as p
import time
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.End()

physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(.1)


p.disconnect()
