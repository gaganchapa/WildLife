import streamlit as st
# import emoji
# st.divider()
# st.markdown(
#     "<h1 style='text-align: center; color: #1f77b4;'>Analytics Dash Board </h1>",
#     unsafe_allow_html=True
# )
# st.divider()
# st.markdown("")
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
# import streamlit as st
col1, col2 = st.columns(2)


with col1:
    st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 150%;'>Real-Time Elephant Detection and Monitoring</h1>",
        unsafe_allow_html=True
    )
    # chart_data = pd.DataFrame(
    #    [[10.783018, 76.686264],[10.790671, 76.677695],[]],
    #    columns=['lat', 'lon'])
    chart_data2 = pd.read_csv("D:\\all\\Train_Elephant\\streamlit-yolo-master\\pages\\Miine.csv")

    st.map(chart_data2)

with col2:
    
    st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 150%;'>Distribution of Detected Elephants by Pole Location</h1>",
        unsafe_allow_html=True
    )


    chart_data = pd.DataFrame(
    {
        "Pole": [1,2,3,4,5,6,7,8,9,10,11,12],
        "Count": [1,2,2,1,0,0,1,0,0,3,4,0]
    }
    )

    st.bar_chart(chart_data, x="Pole", y="Count")

    with st.container():
        total_count = chart_data["Count"].sum()
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Total Elephants Detected ", value=total_count)
        col3.metric(label="Failure",value ="Pole 13")
        col2.metric(label="Live Elphant Detection",value="Pole 2")
col3, col4 = st.columns(2)
with col3:
    
    st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 150%;'>3D Real-Time Elephant Detection and Monitoring</h1>",
        unsafe_allow_html=True
    )
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=10.783018,
            longitude=76.686264,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data2,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data2,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))



with col4:
    import os, random
    import wandb
    import streamlit as st
    import streamlit.components.v1 as components 

    # from utils import WORDS
    st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 150%;'>Realtime Monitoring of AI Model</h1>",
        unsafe_allow_html=True
    )
    project = "YOLOv8"
    entity = "gagan_new"

    HEIGHT = 510

    def get_project(api, name, entity=None):
        return api.project(name, entity=entity).to_html(height=HEIGHT)

    # st.title("The wandb Dashboard 👇")

    # run_name = "-".join(random.choices(WORDS, k=2)) + f"-{random.randint(0,100)}"

    # # Sidebar
    # sb = st.sidebar
    # sb.title("Train your model")
    # wandb_token = sb.text_input("paste your wandb Api key if you want: https://wandb.ai/authorize", type="password")

    # wandb.login(key=wandb_token)
    wandb.login(anonymous="must")
    api = wandb.Api()

    # st.success(f"You should see a new run named **{run_name}**, it\'ll have a green circle while it\'s still active")

    # render wandb dashboard
    components.html(get_project(api, project, entity), height=HEIGHT)

    # run params
    # runs = 1
    # epochs = sb.slider('Number of epochs:', min_value=100, max_value=500, value=100)