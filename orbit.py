import numpy as np
import math


class Orbit():

    def __init__(self):
        #self.e_vec = np.array([0, 0, 0])
        #self.h_vec = np.array([0, 0, 0])
        #self.n_vec = np.array([0, 0, 0])
        #self.h = 0
        #self.E = 0
        #self.Omega = 0
        #self.omega = 0
        #self.i = 0
        #self.e = 0
        #self.a = 0
        #self.nu = 0
        #self.Pi = 0
        #self.p = 0
        #self.r_vec = np.array([0, 0, 0])
        #self.v_vec = np.array([0, 0, 0])
        #self.r = 0
        #self.v = 0
        return None

    def get_params(self):
        params = {
            "a": self.a,
            "e": self.e,
            "i": self.i,
            "Omega": self.Omega,
            "omega": self.omega,
            "e_vec": self.e_vec,
            "h_vec": self.h_vec,
            "n_vec": self.n_vec,
            "nu": self.nu,
            "Pi": self.Pi,
            "h": self.h,
            "r_vec": self.r_vec,
            "r": self.r,
            "v_vec": self.v_vec,
            "v": self.v,
            "E": self.E,
            "p": self.p
        }

        return params

    def transf_peri_geo(self, omega, little_omega, i):
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

        return R


    def constants_of_motion(self):
        r = self.r
        v = self.v
        r_vec = self.r_vec
        v_vec = self.v_vec

        self.h_vec = np.cross(r_vec, v_vec)
        self.e_vec = (v**2 - 1./r)*r_vec - (np.dot(r_vec, v_vec))*v_vec
        self.n_vec = np.cross([0,0,1], self.h_vec)

        self.h = np.linalg.norm(self.h_vec)
        self.e = np.linalg.norm(self.e_vec)
        self.n = np.linalg.norm(self.n_vec)

        self.E = 0.5*v**2 - 1./r



    def from_params(self, a, e, Omega, omega, i, nu):
        self.Omega = Omega
        self.omega = omega
        self.i = i
        self.e = e
        self.a = a
        self.nu = nu

        R = self.transf_peri_geo(Omega, omega, i)
        self.p = a*(1. - e**2)
        r = self.p/(1+e*math.cos(nu))

        r_peri = np.array([r*math.cos(nu), r*math.sin(nu), 0])
        r_geo = np.squeeze(np.asarray(np.dot(R, r_peri)))

        v_peri = math.sqrt(1./self.p)*np.array([-math.sin(nu), e+math.cos(nu), 0])
        v_geo = np.squeeze(np.asarray(R.dot(v_peri)))

        self.r_vec = r_geo
        self.v_vec = v_geo
        self.r = np.linalg.norm(self.r_vec)
        self.v = np.linalg.norm(self.v_vec)

        self.constants_of_motion()
        self.Pi = math.acos(self.e_vec[0]/self.e)


    def compute_angles(self):
        i = math.acos(np.dot([0,0,1], self.h_vec)/self.h)
        self.i = i if not np.isnan(i) else 0

        Omega = math.acos(np.dot([1,0,0], self.n_vec)/self.n)
        self.Omega = Omega if not np.isnan(Omega) else 0

        omega = math.acos(np.dot(self.e_vec, self.n_vec)/(self.e * self.n ) )
        self.omega = omega if not np.isnan(omega) else 0

        #Longitude of periapsis
        self.Pi = math.acos(self.e_vec[0]/self.e)



    def from_r_v(self, r_vec, v_vec):
        self.r_vec = r_vec
        self.v_vec = v_vec

        self.r = np.linalg.norm(self.r_vec)
        self.v = np.linalg.norm(self.v_vec)

        self.constants_of_motion()
        self.compute_angles()

        self.nu = math.acos(np.dot(self.e_vec, self.r_vec)/(self.e * self.r))
        self.p = self.h**2
        self.a = self.p/(1. - self.e**2)




    def from_constants_of_motion(self, h_vec, e_vec, n_vec, nu):

        self.nu = nu
        self.h_vec = h_vec
        self.e_vec = e_vec
        self.n_vec = n_vec

        self.h = np.linalg.norm(self.h_vec)
        self.e = np.linalg.norm(self.e_vec)
        self.n = np.linalg.norm(self.n_vec)
        self.p = self.h**2
        self.a = self.p/(1. - self.e**2)


        self.compute_angles()
        self.from_params(self.a, self.e, self.Omega, self.omega, self.i, self.nu)
