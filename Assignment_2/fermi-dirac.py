#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np 
import pylab as pl 
import math

#Ef = 2.0
#k = 0.00008617
#T1 = 300
#T2 = 1000

f = open('Fermi-Dirac.dat','w')
x = 1.45
while (x < 2.5):
	y = 1/( (math.exp((x - 2.0)/(0.00008617*300))) + 1)
	f.write( str(x) + '\t' + str(y) + '\n')
	x = x + 0.05
	
x = 1.45
while (x < 2.5):
	y = 1/ ((math.exp((x - 2.0)/(0.00008617*1000))) + 1)
	f.write( str(x) + '\t' + str(y) + '\n')
	x = x + 0.05
   	
f.close()

