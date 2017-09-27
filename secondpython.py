import numpy
import matplotlib.pyplot
import glob

print('analyze my data')

#-----------------------

def analyze(filename):
	'''
	given a filename, import its numerical array and produce three plots, of average, 	max and min across axis 0 of the data, and arrange the plots in a figure.
	'''
	
	data = numpy.loadtxt(fname=filename, delimiter=',')
	
	data = centre(data, 200)
	
	fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
	
	axes1 = fig.add_subplot(1, 3, 1)
	axes2 = fig.add_subplot(1, 3, 2)
	axes3 = fig.add_subplot(1, 3, 3)

	axes1.set_ylabel('mean')
	axes1.plot(numpy.mean(data, axis=0))

	axes2.set_ylabel('max')
	axes2.plot(numpy.max(data, axis=0))

	axes3.set_ylabel('min')
	axes3.plot(numpy.min(data, axis=0))
	
	fig.tight_layout()
	matplotlib.pyplot.show()

def detect_problems(filename):
	data = numpy.loadtxt(fname = filename, delimiter=',')

	if numpy.max(data, axis=0) [0] == 0 and numpy.max(data, axis=0) [20] == 20:
		print('suspicious looking maxima')
	elif numpy.sum(numpy.min(data, axis=0)) == 0:
		print('minima add up to zero')
	else:
		print('seems ok')
#-----------------------

def centre(data, desired):
	're-centres data around the desired value'
	return (data - numpy.mean(data)) + desired

#-----------------------

filenames = glob.glob('../data/inflammation-*.csv')

for file in filenames [:3]:
	print(file)
	analyze(file)
	detect_problems(file)
