
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d 
# import data
V  = []
BV = []

V2  = [-5.8,-4.1,-1.1,0.7,2.0,2.6,3.4,4.4,5.1,5.9,7.3,9.0,11.8]
BV2 = [-0.35,-0.31,-0.16,0.00,0.13,0.27,0.42,0.58,0.70,0.89,1.18,1.45,1.63]

SGV  = [1.1,0.7,0.5,-0.2,-0.4,-0.8,-6.4,-5.0,-5.0,-5.0]
SGBV = [0.65,0.85,1.07,1.41,1.60,1.85,-0.25,-1.39,1.70,1.94]

# to ignore the first line
firstline = 1

def printdata():
	print(len(V))
	print(V)
	print(len(BV))
	print(BV)
	
# add data to lists in correct format	
def add_to_lists(str):
	if(firstline == 1):
		return
	data = str.split(" ")
	data[1] = data[1].rstrip()
	print(data)
	BV.append(float(data[0]))
	V.append(float(data[1])-3)

# open file and read in data, ignore the first line
with open('C:\My code\Hyades_VB_data.prn') as f:
	for line in f:
		add_to_lists(line)
		firstline = 0
		
# printing for debugging		
#printdata()

print("V maximum: " + str(max(V)) + " V Minimum: " + str(min(V)))
print("BV maximum: " + str(max(BV)) + " BV Minimum: " + str(min(BV)))

# plot data give from file
plt.figure(1)
plt.title("Hyades Cluster Colour Magnitude Diagram, V vs B-V")
plt.xlabel("B - V")
plt.ylabel("V")
plt.gca().invert_yaxis()          # invert axis so in descending order
plt.plot(BV,V,'r.')

# plot data from Handout
plt.figure(2)
plt.title("Main Sequence Colour Magnitude Diagram, V vs B-V")
plt.xlabel("B - V")
plt.ylabel("V")
plt.gca().invert_yaxis()          # invert axis so in descending order
plt.plot(BV2,V2,'ro', label='Main Sequence Stars')
plt.plot(SGBV,SGV,'bx',label='Giant and Super Giant Stars')
plt.legend(loc='lower left')

# draw smooth line; using spline(higher power=more accurate line) cubic
x_new = np.linspace(min(BV2), max(BV2), 1000)
f = interp1d(BV2, V2, kind='cubic')
y_smooth = f(x_new)
plt.plot(x_new, y_smooth)

plt.figure(3)
plt.title("")
plt.xlabel("B - V")
plt.ylabel("V")
plt.gca().invert_yaxis()          # invert axis so in descending order
plt.plot(BV2,V2,'r.', label='Main Sequence Stars')
plt.plot(BV,V,'g.', label='Hyades Cluster stars')
plt.plot(SGBV,SGV,'bx',label='Giant and Super Giant Stars')
plt.legend(loc='lower left')


plt.show()
