import pyrosim.pyrosim as pyrosim

length =1
width = 1
height = 1
x=0
y=0
z=.5

pyrosim.Start_SDF("boxes.sdf")

for i in range(20):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z+i] , size=[length,width,height])
    length = .9 * length
    width = .9 * width
    height = .9 * height
    
pyrosim.End()