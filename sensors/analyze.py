import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValue.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValue.npy')
matplotlib.pyplot.plot(backLegSensorValues, label="back", linewidth=4)
matplotlib.pyplot.plot(frontLegSensorValues, label="front")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()