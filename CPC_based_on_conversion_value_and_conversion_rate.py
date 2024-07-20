import streamlit as st
import numpy as np


def CPC_based_on_conv_valu_and_conv_rate():
    with st.container(border=True):
        st.html('<h6>Based on conversion value and conversion rate</h6>')
        col_equation, col_non_equation = st.columns([1, 10])
        with col_equation:
            st.latex(r'''
                        \begin{equation*}
                        \begin{aligned}
                        \text{CPC} = \left(\frac{\text{conversion value}}{\text{target ROAS}}\right) * \text{conversion rate}
                        \end{aligned}
                        \end{equation*}
                        ''')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            with st.container(border=True, height=100):
                conv_value = st.number_input('Conversion value',
                                             min_value=0.0,
                                             step=0.01,
                                             value=3.25,
                                             placeholder="Type a number..."
                                             )

        with col2:
            with st.container(border=True, height=100):
                tROAS = st.number_input('Target ROAS (if you type 400, this means 400%) ',
                                        min_value=0,
                                        step=1,
                                        value=400,
                                        placeholder="Type a number..."
                                        )

        with col3:
            with st.container(border=True, height=100):
                conv_rate = st.number_input('Conversion rate',
                                            min_value=0.0,
                                            max_value=1.0,
                                            step=0.01,
                                            value=0.09,
                                            placeholder="Type a number..."
                                            )

        with col4:
            with st.container(border=True, height=100):
                if conv_value is not None and tROAS is not None and conv_rate is not None:
                    calculated_CPC = np.round(conv_value / (tROAS / 100) * conv_rate, 3)

                    st.write('Max CPC:')
                    st.write(calculated_CPC)


                else:
                    st.warning('Please provide a value for conversion value, conversion rate and target ROAS')