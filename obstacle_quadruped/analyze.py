import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/Back_Leg.npy')
frontLegSensorValues = numpy.load('data/Front_Leg.npy')
targetAnglesFront = numpy.load('data/FrontLeg.npy')
targetAnglesBack = numpy.load('data/BackLeg.npy')
matplotlib.pyplot.plot(backLegSensorValues, label="back", linewidth=4)
matplotlib.pyplot.plot(frontLegSensorValues, label="front")
matplotlib.pyplot.plot(targetAnglesFront, label="FrontAngles")
matplotlib.pyplot.plot(targetAnglesBack, label="BackAngles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()