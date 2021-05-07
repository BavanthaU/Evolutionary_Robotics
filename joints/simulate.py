import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
p.setGravity(0,0,-9.8)

for i in range(1000):
    p.stepSimulation()
    time.sleep(.1)


p.disconnect()
