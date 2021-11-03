import streamlit as st
import pandas as pd
import numpy as np
from streamlit_apex_charts import (
                                    line_chart,
                                    bar_chart,
                                    area_chart,
                                    pie_chart,
                                    donut_chart,
                                    radar_chart,
                                    mixed_chart,
                                    scatter_chart,
                                    polar_area_chart,
                                    radial_bar_chart)

def app(data):
    st.title('Streamlit Apex Charts Demo')
    st.write('### Getting Started')
    df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)),columns=['Apple', 'Microsoft', 'Google'])
    with st.expander('Dataframe'):
        st.dataframe(df)

    with st.expander('Line Chart Help'):
        st.help(line_chart)
    line_chart('Zoomable Line Chart', df)

    with st.expander('Bar chart Help'):
        st.help(bar_chart)
    bar_chart('Bar Chart', df)
    bar_chart('Stacked Bar Chart', df, stacked=True)
    bar_chart('Horizontal Bar Chart', df, horizontal=True, stacked=True)

    with st.expander('Area Chart Help'):
        st.help(area_chart)
    area_chart('Area Chart', df)
    area_chart('Stacked Area Chart', df, stacked=True)

    with st.expander('Pie Chart Help'):
        st.help(pie_chart)
    pie_chart('Pie Chart', df)

    with st.expander('Donut Chart Help'):
        st.help(donut_chart)
    donut_chart('Donut Chart', df)

    with st.expander('Radar Chart Help'):
        st.help(radar_chart)
    radar_chart('Radar Chart', df)

    with st.expander('Mixed Chart Help'):
        st.help(mixed_chart)
    mixed_chart('Mixed Chart', df, plot_types={
        'Google':'line',
        'Apple':'column',
        'Microsoft':'area'
    })

    with st.expander('Scatter Chart Help'):
        st.help(scatter_chart)
    scatter_chart('Scatter Chart', df)

    with st.expander('Polar Area Chart Help'):
        st.help(polar_area_chart)
    polar_area_chart('Polar Area Chart', df)

    with st.expander('Radial Bar Chart Help'):
        st.help(radial_bar_chart)
    radial_bar_chart('Radial Bar Chart', df)

