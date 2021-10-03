import streamlit as st

def app(data):
    st.title('Streamlit Radial Demo')
    st.write('### Getting Started')
    with st.echo():
        from st_radial import st_radial
        import random
        cols = st.columns(3)
        with cols[0]:
            st_radial('Metric 1', value=random.randrange(10, 100))
        with cols[1]:
            st_radial('Metric 2', value=random.randrange(10, 100))
        with cols[2]:
            st_radial('Metric 3', value=random.randrange(10, 100), start_angle=0)