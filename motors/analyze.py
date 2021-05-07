import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValue.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValue.npy')
targetAnglesFront = numpy.load('data/targetAnglesFront.npy')
targetAnglesBack = numpy.load('data/targetAnglesBack.npy')
# matplotlib.pyplot.plot(backLegSensorValues, label="back", linewidth=4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="front")
matplotlib.pyplot.plot(targetAnglesFront, label="FrontAngles")
matplotlib.pyplot.plot(targetAnglesBack, label="BackAngles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()