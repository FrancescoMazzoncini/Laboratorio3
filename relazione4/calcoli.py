import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import uncertainties 
from uncertainties import unumpy


h_fe = ufloat(170, 10)
V_BE = ufloat(0.605, 0.004)
V_CC = ufloat(20.2, 0.1)
R_1 = ufloat(179000,1000)
R_2 = ufloat(18000, 100)
R_C = ufloat(9950, 90)
R_E = ufloat(987, 8)

Vpart = V_CC * (R_2/(R_1+R_2))

print("Vpart = ", Vpart, "\n")


V_CE = ufloat(7.50, 0.04)
V_RC = ufloat(11.62, 0.05)
I_C = V_RC/R_C

print("I_C = ", I_C, "\n")

I_Cteo = (Vpart - V_BE)/R_E
V_CEteo = V_CC - (R_C+R_E)*I_C

print("I_Cteo = ", I_Cteo, "\n")
print("V_CEteo = ", V_CEteo, "\n")


V_E = I_Cteo*R_E
V_C = V_CC-I_Cteo*R_C
V_B = ufloat(1.77, 0.01)

print("V_E = ", V_E, "\n")
print("V_C = ", V_C, "\n")


V_OUT1 = ufloat(6.44, 0.02)
R_S = ufloat(18.1, 0.1)
V_OUT2 = ufloat(2.94, 0.02)
R_IN = R_S*1/(V_OUT1/V_OUT2 -1)
print("R_IN = ", R_IN, "\n")

V_OUT1 = ufloat(9.80, ((0.02)**2+(0.03*9.80)**2)**0.5)
R_L = ufloat(10.05, 0.08)
V_OUT2 = ufloat(5.04, ((0.02)**2+(0.03*5.04)**2)**0.5)
R_OUT = R_L*(V_OUT1/V_OUT2 - 1)
print("R_OUT = ", R_OUT, "\n")


I_B = I_C/h_fe
R_INteo = 1/(1/R_1+1/R_2+ 1/(V_BE/I_B+h_fe*R_E))

print("R_INteo = ", R_INteo, "\n")

#Caduta di tensioni su R1 e R2:
VR_2 = V_B
VR_1 = V_CC - V_B
I_2 = VR_2/R_2
I_1 = VR_1/R_1
I_B = I_2-I_1
print("I_1 = ", I_2, "\n")
print("I_2 = ", I_1, "\n")
print("I_B = ", I_B, "\n")

#Calcolo di I_B attesa:
I_Bteo = I_C/h_fe
print("I_B teorica = ", I_C/h_fe)

#Calcolo della resistenza h_ie utilizzando il valore di I_b misurato
print("h_ie = ", V_BE/I_Bteo, "\n")
#Non mi torna questo valore







 

