import streamlit as st
import re

def get_video_id_from_url(url):
    try:
        return re.findall(r'v=(.*?)&', url)[0]
    except:
        try:
            return re.findall(r'v=(.*)', url)[0]
        except:
            try:
                return re.findall(r'.be/(.*)', url)[0]
            except:
                return False

def get_ad_free_url(id, allow_controls=True, modest_branding=True):
    modified_url = "https://www.youtube.com/embed/{0}"
    if allow_controls:
        modified_url += "?controls=1"
    if modest_branding:
        modified_url += "&modestbranding=1"
    return modified_url.format(id)

def app(data):
    st.title('Youtube Ad-free ▶')
    video_url = st.text_input('Enter video url')
    if video_url:
        video_id = get_video_id_from_url(video_url)
        if video_id:
            st.components.v1.iframe(get_ad_free_url(video_id),height=600)
        else:
            st.warning("😥 Sorry that url didn't work, maybe try another one?")