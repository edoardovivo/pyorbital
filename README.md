# pyorbital
Jupyter notebook with widget to plot orbits and play with the parameters. There are 3 ways to plot an orbit: from orbit parameters, from position and velocity, and from constants of motion.

We refer to the text "Fundamentals of Astrodynamics" by Bate, Mueller, and White, for the notation and the definition of the quantities. We especially refer to figure 2.3.1 of the text for a visual description of all the parameters.


The three basis vectors, I,J,K, are the unit vectors of the coordinate system, in this case the Geocentric-Equatorial system. Their origin is the center of the Earth. I points toward the vernal equinox, K points toward the North Celestial Pole, and J points toward the first point of winter. I and J are in the fundamental plane, in this case the equatorial plane, and K is perpendicular to it. These coordinates do not rotate with the Earth, but their origin does remain at the Earth’s center as the Earth orbits the Sun. The three vectors h, e, and n describe the orbit. They share the same origin with the basis vectors. The specific angular momentum vector, h, is perpendicular to the orbital plane, the eccentricity vector, e, points toward perigee, and the node vector, n points toward the
ascending node.



### From Orbital Parameters

![From_params](https://github.com/edoardovivo/pyorbital/blob/develop/img/from_params.png)

In this case, it is possible to specify the following:

* a, the semi-major axis, a constant describing the size of the orbit
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
* n_vec: the line of nodes
