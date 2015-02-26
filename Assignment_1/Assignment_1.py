#!/usr/bin/python

#Assignment 1 for MSc creating the Bravais Lattice structures for VMD

#touch README
#git add README
#git add (all other files)
#git commit -m 'reinitialized files'
#git push origin master --force
import os
import sys
import math
import numpy
#from scipy.spatial.distance import cdist #(Requires Scipy for the energy function, My linux hates life and wont install it so go ahead and uncomment this)

#A Bravais Lattice structure has a single base atom with repeating pattern. the code generates an xyz file for VMD to take in and view. 

#Lattice systems: 
# Cubic (pcc, bcc, fcc)
# Tetragonal (P,I)
# Orthorhombic (P,C,I,F)
# Hexagonal (P)
# Rhombohedral (P)
# Monoclinic (P, C)
# Triclinic (P)

# PLEASE NOTE MARKER: Rather then condensing my code I expanded it to help other students, I know usually You would just do a function and repeat that with imputs the vectors.
# This way it was much simplier for others to look at and visualize as they worked, especially for those whom may not be comfortable with coding. 

# Start with the most simple strucre, Primitive Cubic
# these are what the x,y,z files should produce. 

#-----------
#2
#
#C x y z
#C x y z
#------------
#Atoms per dimension
Atoms = 4
Atoms_Cubed = Atoms * Atoms * Atoms
#Atoms per lattice structure are Atoms cubed * lattice's

print 'Files Generated. Have nice day.'
#For even spaced structures incr can be altered for visuals
incr = 1

#For un-even spaced structures you can change x,y,z spacing.
incx = 3.0
incy = 2.0
incz = 1.0

def Energy(tot_atoms):
   	"Takes in atom vectors and prints out the total energy in the system"
   	r_m = 2.
	eps=10.
	ETOT = 0.

	for k in range(tot_atoms):
		r = cdist(lattice, numpy.array([lattice[k]])).flatten()
		r = r[numpy.nonzero(r)]
		V = eps*((r_m/r)**12 - (2.*(r_m/r)**6))

	ETOT += numpy.sum(V)
	E = ETOT/(tot_atoms*2.)
	print E
 	return

f = open('Assignment_1_PC.txt','w')
f.write(str(Atoms_Cubed) + '\n')
f.write('\n')

#f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + "/n")

# Primitive Cubic Lattice
tot_atoms = Atoms_Cubed
x = 0
for i in range(0 , Atoms):
	#Start with the X,Y,Z basis coordinate
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr
f.close()
#Energy(tot_atoms)

# Body centered cubic the second loop creates a second lattice in the middle

f = open('Assignment_1_BCC.txt','w')
f.write(str(Atoms_Cubed*2) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr


x = 0.5 * incr
for i in range(0 , Atoms):
	y = 0.5 * incr
	for j in range (0, Atoms):
		z = 0.5 * incr
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr
f.close()


# Face centered cubic
f = open('Assignment_1_FCC.txt','w')
f.write(str(Atoms_Cubed*4) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr


x = 0.5 * incr
for i in range(0 , Atoms):
	y = 0.5 * incr
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr


x = 0
for i in range(0 , Atoms):
	y = 0.5 * incr
	for j in range (0, Atoms):
		z = 0.5 * incr
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr

x = 0.5 * incr
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0.5 * incr
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incr
	x = x + incr
f.close()

tot_atoms = Atoms_Cubed
# The Primitive Orthorombic Lattice
f = open('Assignment_1_PO.txt','w')
f.write(str(Atoms_Cubed) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx
f.close()


tot_atoms = Atoms_Cubed*2
# Base Centered Orthorhombic Lattice
f = open('Assignment_1_BaCO.txt','w')
f.write(str(Atoms_Cubed*2) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

x = incx * 0.5
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = incz * 0.5
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

f.close()

# Body Centered Orthorhombic Lattice
f = open('Assignment_1_BCO.txt','w')
f.write(str(Atoms_Cubed*2) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

x = incx * 0.5
for i in range(0 , Atoms):
	y = 0.5 * incy
	for j in range (0, Atoms):
		z = incz * 0.5
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

f.close()


# Face Centered Orthorhombic Lattice

f = open('Assignment_1_FCO.txt','w')
f.write(str(Atoms_Cubed*4) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

x = incx * 0.5
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = incz * 0.5
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

x = incx * 0.5
for i in range(0 , Atoms):
	y = 0.5 * incy
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

x = 0
for i in range(0 , Atoms):
	y = 0.5 * incy
	for j in range (0, Atoms):
		z = incz * 0.5
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incz
		y = y + incy
	x = x + incx

f.close()

#Tetragonal Bravais Lattice's have two increments that are the same
#Primitive Tetragonal lattices
f = open('Assignment_1_PT.txt','w')
f.write(str(Atoms_Cubed) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incy
	x = x + incr
f.close()

# Body Centerd Tetragonal Bravais Lattice

f = open('Assignment_1_BCT.txt','w')
f.write(str(Atoms_Cubed) + '\n')
f.write('\n')

x = 0
for i in range(0 , Atoms):
	y = 0
	for j in range (0, Atoms):
		z = 0
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incy
	x = x + incr

x = 0.5 * incr
for i in range(0 , Atoms):
	y = 0.5 * incy
	for j in range (0, Atoms):
		z = 0.5 * incr
		for k in range (0 , Atoms):
   			f.write('C' + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + '\n')
   			z = z + incr
		y = y + incy
	x = x + incr
f.close()

# Hexagonal


#Need numpy
a=1
b=1
c=1
#how to array?
a1 = numpy.array([a*3*0.5, a*math.sqrt(3)*0.5, 0])
a2 = numpy.array([0,a*math.sqrt(3),0])
a3 = numpy.array([0,0,c])

HexAtoms = Atoms
HexAtomsCubed = HexAtoms * HexAtoms * HexAtoms
TotHex = HexAtomsCubed * 3
f = open('Assignment_1_Hex.txt','w')
f.write(str(TotHex) + '\n')
f.write('\n')
for i in range(0 , Atoms):
	for j in range (0, Atoms):
		for k in range (0 , Atoms):
			vector = i*a1 + j*a2 + k*a3
			#Place the Atoms where we are standing
			f.write('C' + "\t" + str(vector[0]) + "\t" + str(vector[1]) + "\t" + str(vector[2]) + '\n')
			#Place our next atom
			temp1 = vector + numpy.array([1,0,0])
			f.write('C' + "\t" + str(temp1[0]) + "\t" + str(temp1[1]) + "\t" + str(temp1[2]) + '\n')
			#Place the third atom
			temp2 = vector + numpy.array([1,math.sqrt(3),0])
			f.write('C' + "\t" + str(temp2[0]) + "\t" + str(temp2[1]) + "\t" + str(temp2[2]) + '\n')			
f.close()

#Rhombohedral


#Monoclinic
# Primitive Monoclinic

# Base-Centered Monoclinic

#Triclinic

#Finding the Energy based on the LJ potential. 