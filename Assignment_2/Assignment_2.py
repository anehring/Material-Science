#!/usr/bin/env python
#Question 3

#Imports


f = open('Spring_Position.txt','w')
g = open('Spring_KE.txt','w')
h = open('Spring_PE.txt','w')
j = open('Spring_TE.txt','w')

#Constants
k = 20.0
mass = 3.0
x_0 = 4.0
x = 2.0
v = 0.0


time = 10.0
dt = 0.001 
time_steps = time / dt
t = 0.0

print (str(time_steps) + " timesteps" )
print ('k equals ' + str(k) + '\n' + "x_o is " + str(x_0) + "\n")

flag = 0

while (t < time):
	#force = mass * acceleration
	acceleration = -k * (x-x_0) / mass
	v = v + acceleration*dt
	x = x + v*dt

	#Kinetic Energy = 1/2 mv*v
	KE = 0.5*mass*(v**2)
	PE = 0.5*k*(x-x_0)**2
	TE = float(KE) + float(PE)

	f.write(str(t) + '\t' + str(x) +'\n')
	g.write(str(t) + '\t' + str(KE) + '\n')
	h.write(str(t) + '\t' + str(PE) + '\n')
	j.write(str(t) + '\t' + str(TE) + '\n')


	t = t + dt
f.close()
g.close()
h.close()
j.close()

# Second mass connected to the first string. 

k = 20.0
mass = 3.0
x_0 = 4.0
x1 = 2.0
v1 = 0.0
x2 = 8.0
t = 0.0
v2 = 0.0

l = open('TS_1.txt','w')
l2 = open('TS_2.txt','w')

while (t < time):
	#force = mass * acceleration
	f1 = -k*(x1-x_0) + k*(x2-x1-2)
	a1 = f1 / mass
	v1 = v1 + a1*dt
	x1 = x1 + v1*dt

	f2 = -k*(x2 - x1 - 2)
	a2 = f2 / mass
	v2 = v2 + a2*dt
	x2 = x2 + v2*dt
	l.write(str(t) + '\t' + str(x1) + '\n')
	l2.write(str(t) + '\t' + str(x2) + '\n')

	t=t+dt

l.close()
l2.close()


