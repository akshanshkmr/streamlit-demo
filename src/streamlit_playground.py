import streamlit as st
from streamlit_ace import st_ace

def security_check(code):
    import re
    restricted_modules = ['os','sys','pathlib']
    for module in restricted_modules:
        if re.search("import.*" + module, code) or re.search("from.*" + module, code):
            raise ImportError(module)
    return True

def app(data):
    st.title('Streamlit Playground')
    with st.form(key='editor'):
        code = st_ace(
            theme='dracula',
            auto_update=True,
            language='python',
            height=500,
            value='# learn streamlit on the fly\n')
        if st.form_submit_button('Run'):
            if security_check(code):
                exec(code)