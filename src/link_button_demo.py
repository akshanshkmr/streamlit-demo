import streamlit as st

def app(data):
    st.title('Streamlit Link Button Demo')
    st.write('### Getting Started')
    with st.echo():
        from link_button import link_button
        _clicked = link_button(name = 'Click Me!', url = 'https://docs.streamlit.io/en/stable/')
        if _clicked:    
            st.balloons()