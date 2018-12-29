import numpy as np
import math


#Constant mu
mu = 1
mu_1 = 3.986004418e+14

#Orbital parameters
a = 6
e = .5

#Angles in radians!
i = 0
little_omega = 0
omega = 0
nu = 2.618

#Transformation matrix from perifocal to geocentric equatorial
IdotP = math.cos(omega)*math.cos(little_omega) - math.sin(omega)*math.sin(little_omega)*math.cos(i)
IdotQ = -math.cos(omega)*math.sin(little_omega) - math.sin(omega)*math.cos(little_omega)*math.cos(i)
IdotW = math.sin(omega)*math.sin(i)

JdotP = math.sin(omega)*math.cos(little_omega) - math.cos(omega)*math.sin(little_omega)*math.cos(i)
JdotQ = -math.sin(omega)*math.sin(little_omega) + math.cos(omega)*math.cos(little_omega)*math.cos(i)
JdotW = -math.cos(omega)*math.sin(i)

KdotP = math.sin(little_omega)*math.sin(i)
KdotQ = math.cos(little_omega)*math.sin(i)
KdotW = math.cos(i)

R = np.matrix([[IdotP, IdotQ, IdotW], [JdotP, JdotQ, JdotW], [KdotP, KdotQ, KdotW]])

print(R)
#Computing position and velocity
p = a*(1. - e**2)
r = p/(1+e*math.cos(nu))

print("r : {}".format(r))

r_peri = np.array([r*math.cos(nu), r*math.sin(nu), 0])
#print(r_peri)

r_geo = np.squeeze(np.asarray(np.dot(R, r_peri)))
print("r_geo: {}".format(r_geo))

v_peri = math.sqrt(mu/p)*np.array([-math.sin(nu), e+math.cos(nu), 0])
#print(v_peri)

v_geo = np.squeeze(np.asarray(R.dot(v_peri)))
print("v_geo: {}".format(v_geo))

v = math.sqrt(mu/p)*math.sqrt(1 + e**2 + 2*e*math.cos(nu))

print("v: {}".format(v) )
#In km/s
print("v (km/s): {}".format(v*7.9))

#Angular momentum
h_geo = np.cross(r_geo, v_geo)
print("h_geo : {}".format(h_geo))
print("h : {}".format(np.linalg.norm(h_geo)))

#Eccentricity vector
e_geo = (v**2 - 1./r)*r_geo - (np.dot(r_geo, v_geo))*v_geo
print("e_geo : {}".format(e_geo))
print("e : {}".format(np.linalg.norm(e_geo)))


#Node vector
n_geo = np.cross([0,0,1], h_geo)
print("n_geo : {}".format(n_geo))
print("n : {}".format(np.linalg.norm(n_geo)))



#Let's add delta_v
delta_v = 1e-15
v_new = v + delta_v
v_new_peri = np.array([v_new*math.cos(nu), v_new*math.sin(nu), 0])
v_new_geo = np.squeeze(np.asarray(R.dot(v_new_peri)))
print("v_new_geo : {}".format(v_new_geo))
print("v_new  {}".format(np.linalg.norm(v_new_geo)))



h_new = np.cross(r_geo, v_new_geo)
print(h_new)
