import streamlit as st
import numpy as np


def CPC_based_on_rev_per_click():
    with st.container(border=True):
        st.html('<h6>Based on revenue per click data</h6>')
        col_equation, col_non_equation = st.columns([1, 10])
        with col_equation:
            st.latex(r'''
                        \begin{equation*}
                        \begin{aligned}
                        \text{CPC} = \frac{\text{cost}}{\text{click}}
                                   = \frac{\text{revenue * cost}}{\text{revenue * click}} 
                                   = \frac{ \frac{\text{revenue}}{\text{click}}} {\frac{\text{revenue}}{\text{cost}}}
                                   = \frac{\text{revenue per click}}{\text{target ROAS}}
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
                    calculated_CPC = np.round(rev_per_click / (tROAS / 100), 3)

                    st.write('Max CPC:')
                    st.write(calculated_CPC)


                else:
                    st.warning('Please provide a value for revenue per click and target ROAS')