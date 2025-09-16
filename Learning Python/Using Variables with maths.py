import math as m

G = 6.67e-11
Me = 5.972e24 # you have to put units in as comment, if i were to put kg after this value and try print it wouldnt work
Re = 6.378e6 # you have to put units in as comment, if i were to put kg after this value and try print it wouldnt work
h = 23456 # height in meters

g = G * Me / (Re + h)**2 

print("g = ", g, " N/kg")

z= m.sqrt(h**2 + Re**2)
print("z = ", z)
theta = 30*m.pi/180
f = m.cos(theta)
print("f = ", f)
