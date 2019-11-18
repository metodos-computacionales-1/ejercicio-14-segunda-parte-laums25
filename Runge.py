import os
import numpy as np
import matplotlib.pyplot as plt
	
plt.figure(1, figsize=(8,4))
plt.subplot(1,3,1)
data = np.loadtxt("datos.dat")

plt.plot(data[:,0], data[:,1])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('yn(0) vs t')

plt.subplot(1,3,2)

plt.plot(data[:,0], data[:,2])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('yn(1) vs t')

plt.subplot(1,3,3)

plt.plot(data[:,1], data[:,2])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('yn(0) vs yn(1)')
plt.savefig("Runge.png")
