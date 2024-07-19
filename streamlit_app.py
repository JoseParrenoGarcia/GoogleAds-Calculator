import streamlit as st
import numpy as np
from CPC_based_on_rev_per_click import CPC_based_on_rev_per_click
from CPC_based_on_conversion_value_and_conversion_rate import CPC_based_on_conv_valu_and_conv_rate
from CPA_calculation import CPA_calculation
from Profit_margins import profit_margins

# ---------------------------------------------------------------------
# HOME PAGE - CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    layout="wide",
)

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
with st.container(border=True):
    st.html('<h5>If you work with manual CPC (or max CPC)</h5>')
    CPC_based_on_rev_per_click()
    CPC_based_on_conv_valu_and_conv_rate()

# ---------------------------------------------------------------------
with st.container(border=True):
    CPA_calculation()

# ---------------------------------------------------------------------
with st.container(border=True):
    profit_margins()




