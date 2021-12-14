#!/usr/bin/python3

import streamlit as st
import pandas as pd
import numpy as np

from text import *
from functions import *

title = 'Why areas matter'

st.title(title)
st.markdown(text_1)

st.markdown(text_2)



power_demand = power_drive(speed, 0.3, 2.5) * efficiency_car

field_length = length_field(power_demand, solar, spacing)

st.markdown(field_length)


#st.metric(label, value, delta=None, delta_color="normal")
