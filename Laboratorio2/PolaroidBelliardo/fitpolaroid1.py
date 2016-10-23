import scipy
import math
import numpy
from scipy.optimize import curve_fit
import pylab

theta, I = pylab.loadtxt('datipolaroid.txt', unpack = 'True')
theta = theta*3.14/180	#conversione da gradi a radianti
Dtheta = numpy.array([0.5*3.14/180 for i in range (len(theta))])
DI = I*0.8%+0.3

def f(x, a, b, c):
	return a+b*(numpy.cos(x+c))**2
#faccio fit
init = (10, 50 , 7.5)
pars, covm = curve_fit(f, theta, I, init, DI)
print(pars)
print(covm)
chi2 = numpy.array((f(theta,pars[0], pars[1], pars[2])-I)**2/DI**2).sum()
ndof = len(theta) - 3
print(chi2/ndof)
#plotto dati
pylab.errorbar(theta, I, DI, Dtheta, linestyle = '', marker = '.', color = 'black')
pylab.xlabel('Angolo (rad)')
pylab.ylabel('Corrente (microA)')
xx = numpy.linspace(0, 6.28, 100)
pylab.plot(xx, f(xx, pars[0], pars[1], pars[2]), color = 'blue')
pylab.show()