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

#what do we need to assume
st.markdown('In order to adress this problem some assumptions need to be done.')

st.markdown('''
    How efficient can we make the fuel from the sun light?\n
    There are several options the first is to produce fuel using energy crops.
    These transform the sunlight into usable energy with the efficy of 0.5 %%.
    Solar cells have a much higher efficy, around 20 %%. \n
    This choice has also implications on the type of car we are using.
    Let us assume that we burn bio fuel in a petrol car and we use the solar
    energy to charge a electric vehilce. The efficy is arround 30 %% and 70%%
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


st.markdown('How fast is the car going?\n')

st.markdown('How much air resistance does the car have?\n')

st.markdown('How far are the cars appart?')




#show the parameters
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Car speed", value= speed, delta= None)
col2.metric(label="Car spacing", value= spacing, delta= None)
col3.metric(label="Car efficiency", value= '%s %%' %(int(eff_car*100)),
            delta= None)
col4.metric(label="Production efficiency", value= '%s %%'
            %(eff_prod*100), delta= None)



power_demand = power_drive(speed * 0.28, 0.3, 2.5) / eff_car

field_length = length_field(power_demand, solar, spacing, eff_prod)


st.metric(label="Width of the side stripe", value= int(field_length), delta= None)
