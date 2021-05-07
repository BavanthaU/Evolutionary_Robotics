import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self, solutionID):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.planeId = p.loadURDF("plane.urdf")
        self.object = p.loadSDF("world"+str(solutionID)+".sdf")

    #return the link orientation & position
    def linkPoisionAndOrientation(self, linkID):
        return p.getBasePositionAndOrientation(self.object[linkID]) 