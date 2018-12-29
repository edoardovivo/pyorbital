import ipywidgets as widgets
import math
import numpy as np

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
