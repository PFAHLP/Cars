#!/usr/bin/python3

import streamlit as st
import pandas as pd
import numpy as np

from text import *
from functions import *

import matplotlib.pyplot as plt

def cars_side():
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

    #show the parameters
    st.metric(label="Car efficiency", value= '%s %%' %(int(eff_car*100)),
                delta= None)
    st.metric(label="Production efficiency", value= '%s %%'
                %round(eff_prod*100, 3), delta= None)
    st.markdown('''
        Since the power demand grows with the speed cubed it is important to
        choose the right speed.
    ''')

    speed = st.slider('How fast is the car going?', 0, 250, 100)

    spacing = st.slider('How far are the cars appart?', 10, 1000, 100)





    power_demand = power_drive(speed * 0.28, 0.3, 2.5) / eff_car

    field_length = length_field(power_demand, solar, spacing, eff_prod)


    st.metric(label="Therefore the side stripe has to be", value= "%s m." %int(field_length), delta= None)

    st.markdown('''
        it does not matter how long the road is, since we grow the crops beside the road.
        This number maybe makes you think. Thinking about the needed areas and the needed energy.
    ''')



    st.latex(r'''
             F = c_w A \frac{1}{2} \rho v^2
         ''')



    chart_data = pd.DataFrame(
         np.array(
         [np.arange(0, 3, 0.1) * speed,
         np.arange(0, 3, 0.1)*eff_car,
         np.arange(0, 3, 0.1)+spacing]
         ).T,
         columns=['speed', 'b', 'c'])

    st.line_chart(chart_data)
