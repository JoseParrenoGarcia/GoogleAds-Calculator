import streamlit as st
import numpy as np


def CPA_calculation():
    st.html('<h5>If you work with target CPA</h5>')

    col_equation, col_non_equation = st.columns([1, 10])
    with col_equation:
        st.latex(r'''
                \begin{equation*}
                \begin{aligned}
                \text{CPA} = \frac{\text{cost}}{\text{acquisition}}
                           = \frac{\text{revenue * cost}}{\text{revenue * acquisition}} 
                           = \frac{ \frac{\text{revenue}}{\text{acquisition}}} {\frac{\text{revenue}}{\text{cost}}}
                           = \frac{\text{revenue per acquisition}}{\text{target ROAS}}
                \end{aligned}
                \end{equation*}
                ''')

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True, height=100):
            rev_per_conv = st.number_input('Revenue per acquisition (or conversion)',
                                           min_value=0.0,
                                           step=0.01,
                                           value=40.25,
                                           placeholder="Type a number..."
                                           )

    with col2:
        with st.container(border=True, height=100):
            tROAS_cpa = st.number_input('Target ROAS (if you type 400, this means 400%)  ',
                                        min_value=0,
                                        step=1,
                                        value=400,
                                        placeholder="Type a number..."
                                        )

    with col3:
        with st.container(border=True, height=100):
            if rev_per_conv is not None and tROAS_cpa is not None:
                calculated_CPA = np.round(rev_per_conv / (tROAS_cpa / 100), 3)

                st.write('tCPA:')
                st.write(calculated_CPA)


            else:
                st.warning('Please provide a value for revenue per acquisition and target ROAS')