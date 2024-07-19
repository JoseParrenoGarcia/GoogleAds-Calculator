import streamlit as st
import numpy as np

def profit_margins():
    st.html('<h5>If you want to determine what your ROAS should be based on profit margins</h5>')

    col_equation, col_non_equation = st.columns([1, 10])
    with col_equation:
        st.latex(r'''
                        \begin{equation*}
                        \begin{aligned}
                        \text{Break even ROAS} = \frac{1}{\text{Average profit margin}}
                        \end{aligned}
                        \end{equation*}
                        ''')

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True, height=100):
            avg_profit_margin = st.number_input('Average profit margin (if you type 400, this means 400%)',
                                                min_value=0.0,
                                                step=0.01,
                                                value=40.0,
                                                placeholder="Type a number..."
                                                )

    with col2:
        with st.container(border=True, height=100):
            if avg_profit_margin is not None:
                calculated_tROAS = np.round(1 / (avg_profit_margin / 100), 3)

                st.write('tROAS:')
                st.write(calculated_tROAS)


            else:
                st.warning('Please provide a value for average profit margin')