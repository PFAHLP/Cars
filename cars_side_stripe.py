#!/usr/bin/python3

import streamlit as st
import pandas as pd
import numpy as np

from text import *
from functions import *

title = 'Why areas matter'

st.title(title)
#some intro
st.markdown(text_1)


st.markdown('''
    In order to adress this problem some assumptions need to be done.

    There are several options the first is to produce fuel using energy crops.
    These transform the sunlight into usable energy with the efficy of 0.1 %.
    Solar cells have a much higher efficy, around 20 %.
    This choice has also implications on the type of car we are using.
    Let us assume that we burn bio fuel in a petrol car and we use the solar
    energy to charge a electric vehilce. The efficy is arround 30 % and 70%
    respectivly.
''')

Production_type = st.selectbox(
     'What kind of Production do you choose?',
     ( 'Bio fuel','Solar cells'))

if Production_type == 'Solar cells':
    eff_car = efficiency_car[1]
    eff_prod = efficiency_prod[1]

else:
    eff_car = efficiency_car[0]
    eff_prod = efficiency_prod[0]

st.markdown('''
    Since the power demand grows with the speed cubed it is important to
    choose the right speed.
''')

speed = st.slider('How fast is the car going?', 0, 250, 100)

spacing = st.slider('How far are the cars appart?', 10, 1000, 100)

#show the parameters
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Car speed", value= speed, delta= None)
col2.metric(label="Car spacing", value= spacing, delta= None)
col3.metric(label="Car efficiency", value= '%s %%' %(int(eff_car*100)),
            delta= None)
col4.metric(label="Production efficiency", value= '%s %%'
            %round(eff_prod*100, 3), delta= None)



power_demand = power_drive(speed * 0.28, 0.3, 2.5) / eff_car

field_length = length_field(power_demand, solar, spacing, eff_prod)


st.metric(label="Therefore the side stripe has to be", value= "%s m." %int(field_length), delta= None)

st.markdown('''
    it does not matter how long the road is, since we grow the crops beside the road
''')



st.latex(r'''
         F = c_w A \frac{1}{2} \rho v^2
     ''')
