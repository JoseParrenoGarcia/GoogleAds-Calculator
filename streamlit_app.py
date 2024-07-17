import streamlit as st
import numpy as np

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

    col_equation, col_non_equation = st.columns([1, 10])
    with col_equation:
        st.latex(r'''
                \begin{equation*}
                \begin{aligned}
                \text{CPC} = \frac{\text{revenue per click}}{\text{target ROAS}}
                \end{aligned}
                \end{equation*}
                ''')

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True, height=100):
            rev_per_click = st.number_input('Revenue per click',
                                            min_value=0.0,
                                            step=0.01,
                                            value=3.25,
                                            placeholder="Type a number..."
                                            )

    with col2:
        with st.container(border=True, height=100):
            tROAS = st.number_input('Target ROAS (if you type 400, this means 400%)',
                                    min_value=0,
                                    step=1,
                                    value=400,
                                    placeholder="Type a number..."
                                    )

    with col3:
        with st.container(border=True, height=100):
            if rev_per_click is not None and tROAS is not None:
                calculated_CPC = np.round(rev_per_click / (tROAS/100), 3)

                st.write('Max CPC:')
                st.write(calculated_CPC)


            else:
                st.warning('Please provide a value for revenue per click and target ROAS')
