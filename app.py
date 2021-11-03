import streamlit as st
from   src.utils.MultiPage import MultiPage
from   src       import (link_button_demo,
                        st_card_demo,
                        st_radial_demo,
                        st_apex_charts_demo,
                        yt_adfree)

def about_dev():
    st.set_page_config(layout='wide')
    st.sidebar.title("About the developer")
    st.sidebar.markdown("""
    #### Hi there, I am Akshansh Kumar <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px">
    ###### Please visit my [github page](https://github.com/akshanshkmr) for more such utilities
    ###### If you liked my work and would like to support me, consider buying me a coffee 😄
    <br><a href="https://www.buymeacoffee.com/akshanshkmr" target="_blank">
    <img class="center" src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a> 
    """,unsafe_allow_html=True)

if __name__ == "__main__":
    about_dev()
    app = MultiPage()
    app.add_app("link_button",link_button_demo.app)
    app.add_app("st_radial",st_radial_demo.app)
    app.add_app("st_card",st_card_demo.app)
    app.add_app("streamlit_apex_charts",st_apex_charts_demo.app)
    app.add_app("yt_ad_free",yt_adfree.app)
    app.run()


