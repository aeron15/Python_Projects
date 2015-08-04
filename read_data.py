# this will load numpy for us
from pylab import *

# load the file and store the result in data
data = np.loadtxt('file.dat')
print data

# compute the plot
plot(data)

# Show it in a new window
show()
