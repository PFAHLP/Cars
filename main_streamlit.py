import streamlit as st
import pandas as pd
import numpy as np

from cars_side_stripe import *

#setup of the page
st.set_page_config(layout="wide")

col1, col2 = st.columns([4,1])
with col1:
    cars_side()
