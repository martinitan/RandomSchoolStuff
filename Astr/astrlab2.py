
import matplotlib.pyplot as plt

# OBAGFKM order, data collected from CLEA
mag      = [7.54,6.60,9.17,5.09,7.97,6.95,8.27,9.05,9.25,10.02,9.70,5.76,6.43,8.60,4.31,10.52]
spectype = ['B6','B6','B6','B6','A1','A1','F0','F5','F5','G2','G2','B6','B6','F0','B6','G2']

#brightness based, out of order
AppMagBright  = [0.58,-0.01,-0.10,1.74,2.20,-3.55,-5.28 ,-2.77,-0.52,2.68,-1.08,5.70,0.59,-0.60,4.85,4.34]
AppSpecBright = ['A0','A1' ,'A2' ,'A3','A7','B1' ,'B2.5','B3' ,'B7' ,'F5','F7' ,'K1','A2','B3','G2','G2' ]
#distance based, out of order
AppMagClose  = [-26.72,11.05,0.01,1.34,9.57  ,13.53 ,7.47,-1.43,12.61 ,13.06,10.44 ,12.29 ,3.73,7.34,11.16,13.03,13.27,15.07,5.2 ,6.03,0.37,8.9 ,9.69  ,8.08  ,11.06 ,4.68,14.9,3.49  ,13.09]
AppSpecClose = ['G2'  ,'M5' ,'G2','K0','M3.5','M5.5','M2','A1' ,'M5.5','M6' ,'M3.5','M5.5','K2','M1','M4' ,'M5' ,'M'  ,'M'  ,'K5','K7','F5','M3','M3.5','M1.5','M3.5','K5','M6','G8.5','M5']

# above lists combined, OBAGFKM order
AppMag2  = [-3.55,-5.28 ,-0.60,-2.77,-0.52,0.58,-1.43,-0.01,-0.10,0.59,1.74,2.20,0.37,2.68,-1.08,4.85,4.34,-26.72,0.01,3.49  ,1.34,5.70,3.73,5.2 ,6.03,13.27,15.07,7.34,8.08  ,7.47,8.9 ,11.06 ,9.69  ,10.44 ,9.57  ,11.16,13.09,13.03,11.05,12.29 ,13.53 ,12.61 ,13.06,14.9]
AppSpec2 = ['B1' ,'B2.5','B3' ,'B3' ,'B7' ,'A0','A1' ,'A1' ,'A2' ,'A2','A3','A7','F5','F5','F7' ,'G2','G2','G2'  ,'G2','G8.5','K0','K1','K2','K5','K7','M'  ,'M'  ,'M1','M1.5','M2','M3','M3.5','M3.5','M3.5','M3.5','M4' ,'M5','M5' ,'M5' ,'M5.5','M5.5','M5.5','M6' ,'M6']

print(len(AppSpec2))
print(100*(5/len(AppSpec2)))

# main sequence line
x = [0,1,2,3,4]
y = [7,7.75,8.5,9.25,10]

# plot data collected via CLEA
plt.figure(1)
plt.title("Magnitude vs Spectral Type, Pleiades data")
plt.xlabel("Spectral Type")
plt.ylabel("Apparent Magnitude")
plt.gca().invert_yaxis()          # invert axis so in descending order
plt.plot(spectype,mag,'r.')
plt.plot(x,y,label='Main Sequence')

# plot data from Textbook appendices
plt.figure(2)
plt.title("Magnitude vs Spectral Type, TextBook data")
plt.xlabel("Spectral Type")
plt.ylabel("Apparent Magnitude")
plt.gca().invert_yaxis()          # invert axis so in descending order
plt.plot(AppSpec2,AppMag2,'r.')

#display the graphs
plt.show()

