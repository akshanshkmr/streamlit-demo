import streamlit as st

def app(data):
    st.title('Streamlit Card Demo')
    st.write('### Getting Started')
    with st.echo():
        from st_card import st_card
        cols = st.columns(3)
        with cols[0]:
            st_card('Orders', value=1200, delta=-45, delta_description='since last month')
        with cols[1]:
            st_card('Competed Orders', value=76.4, unit='%', show_progress=True)
        with cols[2]:
            st_card('Profit', value=45000, unit='($)', delta=48, use_percentage_delta=True, delta_description='since last year')