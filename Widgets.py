
# coding: utf-8

import ipywidgets as widgets
import math
import numpy as np
import rebound
from orbit import Orbit

w_a = widgets.FloatSlider(
                value=1,
                min=1,
                max=10.0,
                step=0.001,
                description='a:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_e = widgets.FloatSlider(
                value=0.5,
                min=0,
                max=1,
                step=0.001,
                description='e:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_i = widgets.FloatSlider(
                value=0.0,
                min=0,
                max=2*math.pi,
                step=0.001,
                description='i:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_Omega = widgets.FloatSlider(
                value=0.0,
                min=0,
                max=2*math.pi,
                step=0.001,
                description='Omega:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_omega= widgets.FloatSlider(
                value=0.0,
                min=0,
                max=2*math.pi,
                step=0.001,
                description='omega:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_nu= widgets.FloatSlider(
                value=0.0,
                min=0,
                max=2*math.pi,
                step=0.001,
                description='nu:',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.5f',
            )

w_h_vec = widgets.Text(
        value='[]',
        placeholder='[1,0,0]',
        description='h:',
        disabled=False
        )

w_e_vec = widgets.Text(
        value='[]',
        placeholder='[1,0,0]',
        description='e_vec:',
        disabled=False
        )

w_n_vec = widgets.Text(
        value='[]',
        placeholder='[1,0,0]',
        description='n_vec:',
        disabled=False
        )



w_r_vec = widgets.Text(
        value='[]',
        placeholder='[1,0,0]',
        description='r:',
        disabled=False
        )

w_v_vec = widgets.Text(
        value='[]',
        placeholder='[1,0,0]',
        description='v:',
        disabled=False
        )


w_E = widgets.FloatText(
        value=0,
        description='E:',
        disabled=False
        )

w_p = widgets.FloatText(
        value=0,
        description='p:',
        disabled=False
        )

w_Pi = widgets.FloatText(
        value=0,
        description='Pi:',
        disabled=False
        )

#del from_params
#del button1
#del from_r_v
#del button2
#del from_constants_of_motion
#del button3



button1 = widgets.Button(description="From Params")
button2 = widgets.Button(description="From position and velocity")
button3 = widgets.Button(description="From constants of motion")


def update_widgets(params):
    w_a.value = params["a"]
    w_e.value = params["e"]
    w_Omega.value = params["Omega"]
    w_omega.value = params["omega"]
    w_i.value = params["i"]
    w_nu.value = params["nu"]
    w_p.value = params["p"]
    w_e_vec.value = str(list(params["e_vec"]))
    w_h_vec.value = str(list(params["h_vec"]))
    w_n_vec.value = str(list(params["n_vec"]))
    w_r_vec.value = str(list(params["r_vec"]))
    w_v_vec.value = str(list(params["v_vec"]))
    w_Pi.value = params["Pi"]
    w_E.value = params["E"]


def plot_orbit(params, sim, fig):

    sim.add(m=1e-5, e=params["e"], a=params["a"],
            inc=params["i"], f=params["nu"],
            Omega=params["Omega"], omega=params["omega"])
    plt.close(fig)
    fig = rebound.OrbitPlot(sim, unitlabel="[AU]", color=True, periastron=True, figsize=(10,8),
                            slices=False)


import matplotlib.pyplot as plt
from IPython.display import display, clear_output


# In[493]:


sim = rebound.Simulation()
sim.add(m=1)


# In[494]:


def from_params(b):
    a = w_a.value
    e = w_e.value
    i = w_i.value
    Omega = w_Omega.value
    omega = w_omega.value
    nu = w_nu.value
    orbit = Orbit()
    orbit.from_params(a, e, Omega, omega, i, nu)
    params = orbit.get_params()
    update_widgets(params)

    with w_out:
        clear_output(wait=True)
        plot_orbit(params, sim, fig)
        plt.show()



# In[495]:


def from_r_v(b):
    r_vec = np.array(eval(w_r_vec.value))
    v_vec = np.array(eval(w_v_vec.value))

    orbit = Orbit()
    orbit.from_r_v(r_vec, v_vec)
    params = orbit.get_params()
    update_widgets(params)

    with w_out:
        clear_output(wait=True)
        plot_orbit(params, sim, fig)
        plt.show()


# In[496]:


def from_constants_of_motion(b):
    h_vec = np.array(eval(w_h_vec.value))
    e_vec = np.array(eval(w_e_vec.value))
    n_vec = np.array(eval(w_n_vec.value))
    nu = w_nu.value

    orbit = Orbit()
    orbit.from_constants_of_motion(h_vec, e_vec, n_vec, nu)
    params = orbit.get_params()
    update_widgets(params)

    with w_out:
        clear_output(wait=True)
        plot_orbit(params, sim, fig)
        plt.show()

button1.on_click(from_params)
button2.on_click(from_r_v)
button3.on_click(from_constants_of_motion)

w_out = widgets.Output()
with w_out:
    fig = plt.figure()



w_def = widgets.HBox([widgets.VBox([w_a, w_e, w_i,
                            w_Omega, w_omega, w_nu, w_Pi,
                            w_p, w_E,
                            w_h_vec, w_e_vec, w_n_vec,
                           w_v_vec, w_r_vec,
                           widgets.HBox([button1, button2, button3])]), w_out])