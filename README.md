# pyorbital
Jupyter notebook with widget to plot orbits and play with the parameters. There are 3 ways to plot an orbit: from orbit parameters, from position and velocity, and from constants of motion.

### From Orbital Parameters

![From_params](https://github.com/edoardovivo/pyorbital/blob/develop/img/from_params.png)

In this case, it is possible to specify the following:

* a, the semi-major axis, a constant describing the size of the orbi
* e, the eccentricity, a constant defining the shape of the orbit
* i, the inclination, the angle between h and K
* Ω, the longitude of the ascending node, an angle in the fundamental plane between I  and the ascending node of the line of nodes, measured counter-clockwise when viewed from the north side of the fundamental plane
* ω, the argument of periapsis, an angle in the orbital plane between the ascending node and periapsis, measured in the direction of the satellite's motion

### From Position and velocity of the satellite

![From_pos_vel](https://github.com/edoardovivo/pyorbital/blob/develop/img/from_pos_vel.png)

The ```coef_r``` and ```coef_v``` parameters are useful if we want to see the effect of doubling the velocity for instance. 

### From Constants of Motion

![From_const_motion](https://github.com/edoardovivo/pyorbital/blob/develop/img/from_const_motion.png)

Here, you can specify:

* h: the angular momentum
* e_vec: the vector eccentricity
* n_vec
