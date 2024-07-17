import streamlit as st

# ---------------------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------------------
with st.container(border=True):
    st.html('<h5>If you work with manual CPC (or max CPC)</h5>')
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.number_input('Revenue per click',
                            min_value=0,
                            max_value=1_000,
                            step=0.01,
                            value=None,
                            placeholder="Type a number..."
                            )

    with col2:
        with st.container(border=True):
            st.write('hello')

    with col3:
        with st.container(border=True):
            st.write('hello')