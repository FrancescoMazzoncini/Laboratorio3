import pylab
import numpy

# data load
x,Dx,y,Dy=pylab.loadtxt('nomefile.txt',unpack=True)

# scatter plot with error bars
pylab.errorbar(x,y,Dy,Dx,linestyle = '', color = 'black', marker = 'o')

# bellurie 
pylab.rc('font',size=16)
pylab.xlabel('$\Delta V$  [V]')
pylab.ylabel('$I$  [mA]')
pylab.title('Data plot w analytical fit')
pylab.minorticks_on()

# set the error and the statistical weight
sigma=Dy
w=1/sigma**2

# determine the coefficients
c1=(w*x**2).sum(); c2=(w*y).sum();c3=(w*x).sum()
c4=(w*x*y).sum(); c5=(w).sum()
Dprime=c5*c1-c3**2

a=(c1*c2-c3*c4)/Dprime
b=(c5*c4-c3*c2)/Dprime

Da=numpy.sqrt(c1/Dprime)
Db=numpy.sqrt(c5/Dprime)

# define the linear function
# note how parameters are entered
# note the syntax
def ff(x, aa, bb):
    return aa+bb*x

# calculate the chisquare for the best-fit funtion
chi2 = ((w*(y-ff(x,a,b))**2)).sum()

# determine the ndof
ndof=len(x)-2

# print results on the console
print(a,Da, b,Db)
print (chi2, ndof)


# prepare a dummy xx array (with 100 linearly spaced points)
xx=numpy.linspace(min(x),max(x),100)

# plot the fitting curve
pylab.plot(xx,ff(xx,a,b), color='red')

# save the plot in pdf format for further use
pylab.savefig('fig2bestfit.pdf') 

# show the plot
pylab.show()

