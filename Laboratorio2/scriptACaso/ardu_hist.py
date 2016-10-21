import pylab as py
import numpy as np

Directory='' # directory where the data file is stored
FileName=(Directory+'') # filename (with directory)

y = py.loadtxt(FileName,unpack='True') # load the data
x = np.arange(0,len(y)) # create an array representing the measurement number
dy = np.ones(len(y)) # create the error bar array (fixed to one digit)

# evaluate the weighted average and standard deviation 
avg=np.average(y,weights=dy)
std=np.std(y,ddof=1)

print('(Weighted) average = ',avg, ' Standard Deviation = ',std)

py.subplot(2,1,1) # prepare and use subplot representation
py.errorbar(x,y,dy,fmt='.',color='blue') # data plot
avga = avg*np.ones(len(y)) # create an array for the avg value
py.plot(x,avga,color='red',linestyle='-.') # superpose the avg value as a horizontal line

# bellurie
py.rc('font',size=14)
py.xlabel('Measurement number',size='16')
py.ylabel('Value  [digit]',size='16')
py.title('Measurements with variable partition',size='18')
py.minorticks_on()
py.legend(['data','avg'],prop={'size':14}) # put a legend (note the ugly format for defining the font size...)
py.ylim(py.ceil(avg)-10,py.ceil(avg)+5) # define the vertical range in a usually correct way (to be eventually adjusted!)
py.tight_layout() # magic instruction to attain correct inter-graph spacing (almost always...)!

py.subplot(2,1,2)
histog=py.hist(y,bins=10,range=(py.ceil(avg)-5,py.ceil(avg)+5),color='gray') # note the way used to determine the range
py.plot([avg,avg],[0,max(histog[0])],color='red',linestyle='-.') # superpose the avg value as a vertical line (note the vertical range)
py.yticks([0,500,1000,1500]) # can be useful not to overfill the vertical axis label with numbers


# bellurie
py.rc('font',size=14)
py.xlabel('Value [digit]',size='16')
py.ylabel('Occurrence',size='16')
py.minorticks_on()
py.tight_layout() # magic instruction to attain correct inter-graph spacing (almost always...)!




py.show()

