import streamlit as st
import cv2
import torch
# from utils.hubconf import custom
import numpy as np
import tempfile
import time
from collections import Counter
import json
import pandas as pd
from ultralytics import YOLO
from model_utils import get_yolo, color_picker_fn, get_system_stat
import subprocess

p_time = 0

st.sidebar.title('Settings')
# Choose the model
model_type = st.sidebar.selectbox(
    'Choose YOLO Model', ('YOLO Model', 'YOLOv8')
)

def run_method(input_data):
    # Run method.py as a subprocess and pass input_data as an argument
    command = ['python', 'client.py', str(input_data)]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running method.py: {e}")

sample_img = cv2.imread('ele_ti.png')

FRAME_WINDOW = st.image(sample_img, channels='BGR', use_column_width="auto")

st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>Wildlife RailGuard 🚂</h1>",
    unsafe_allow_html=True
)

st.markdown("Train-animal collisions pose a significant threat to wildlife and railway infrastructure in forested regions. There is an urgent need for an innovative solution that leverages advanced technologies to detect and prevent collisions, ensuring the safety of wildlife, passengers, and railway operations.")
st.markdown("Current preventive measures are inadequate, leading to tragic loss of animal life, damage to trains, and disruptions in railway services.")
sa = cv2.imread('stat.png')
FRAME_WINDOW = st.image(sa, channels='BGR', use_column_width="auto")

cap = None

if not model_type == 'YOLO Model':
    path_model_file = st.sidebar.selectbox(
        f'path to {model_type} Model:',
        ('Webcam', 'Night Vision')
    )
    if path_model_file == 'Webcam':
        path_model_file = "WebCam.pt"
    else:
        path_model_file = "Night_Vision.pt"
    if st.sidebar.checkbox('Load Model'):
        if model_type == 'YOLOv8':
            model = YOLO(path_model_file)

        # Load Class names
        class_labels = model.names

        # Inference Mode
        options = st.sidebar.radio(
            'Options:', ('Webcam', 'Image', 'Video'), index=1)

        # Confidence
        confidence = st.sidebar.slider(
            'Detection Confidence', min_value=0.0, max_value=1.0, value=0.87)

        # Draw thickness
        draw_thick = st.sidebar.slider(
            'Draw Thickness:', min_value=1,
            max_value=20, value=3
        )
        
        color_pick_list = []
        for i in range(len(class_labels)):
            classname = class_labels[i]
            color = color_picker_fn(classname, i)
            color_pick_list.append(color)

        # Image
        if options == 'Image':
            upload_img_file = st.sidebar.file_uploader(
                'Upload Image', type=['jpg', 'jpeg', 'png'])
            if upload_img_file is not None:
                pred = st.checkbox(f'Predict Using {model_type}')
                file_bytes = np.asarray(
                    bytearray(upload_img_file.read()), dtype=np.uint8)
                img = cv2.imdecode(file_bytes, 1)
                FRAME_WINDOW.image(img, channels='BGR')

                if pred:
                    img, current_no_class = get_yolo(img, model_type, model, confidence, color_pick_list, class_labels, draw_thick)
                    FRAME_WINDOW.image(img, channels='BGR')

                    # Current number of classes
                    class_fq = dict(Counter(i for sub in current_no_class for i in set(sub)))
                    class_fq = json.dumps(class_fq, indent=4)
                    class_fq = json.loads(class_fq)
                    df_fq = pd.DataFrame(class_fq.items(), columns=['Class', 'Number'])
                    
                    # Updating Inference results
                    with st.container():
                        st.markdown("<h2>Inference Statistics</h2>", unsafe_allow_html=True)
                        st.markdown("<h3>Detected objects in current Frame</h3>", unsafe_allow_html=True)
                        st.dataframe(df_fq, use_container_width=True)
                        if any(df_fq["Class"] == "Elephant"):
                            st.markdown("Sending alert🚨")
                            msg = "Elephant detected"
                            run_method(msg)
                        else:
                            st.markdown("Elephant not detected")
                            msg = "Elephant Not detected"
                            run_method(msg)
        
        # Video
        if options == 'Video':
            upload_video_file = st.sidebar.file_uploader(
                'Upload Video', type=['mp4', 'avi', 'mkv'])
            if upload_video_file is not None:
                pred = st.checkbox(f'Predict Using {model_type}')

                tfile = tempfile.NamedTemporaryFile(delete=False)
                tfile.write(upload_video_file.read())
                cap = cv2.VideoCapture(tfile.name)

        # Webcam
        if options == 'Webcam':
            cam_options = st.sidebar.selectbox('Webcam Channel',
                                               ('Select Channel', '0', '1', '2', '3'))
        
            if not cam_options == 'Select Channel':
                pred = st.checkbox(f'Predict Using {model_type}')
                cap = cv2.VideoCapture(int(cam_options))

if (cap != None) and pred:
    stframe1 = st.empty()
    stframe2 = st.empty()
    stframe3 = st.empty()
    while True:
        success, img = cap.read()
        if not success:
            st.error(
                f"{options} NOT working\nCheck {options} properly!!",
                icon="🚨"
            )
            break
        try:
            img, current_no_class = get_yolo(img, model_type, model, confidence, color_pick_list, class_labels, draw_thick)
            FRAME_WINDOW.image(img, channels='BGR')
            
            if current_no_class:
                inner_list = current_no_class[0]
                if inner_list and inner_list[0] == "Elephant":
                    msg = "Elephant detected"
                    run_method(msg)
                else:
                    msg = "Elephant not detected"
                    run_method(msg)
            else:
                input_data = "No classes detected"
                run_method(input_data)
        except Exception as e:
            st.error(f"Error: {e}", icon="🚨")
        
        # FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        
        # Current number of classes
        class_fq = dict(Counter(i for sub in current_no_class for i in set(sub)))
        class_fq = json.dumps(class_fq, indent=4)
        class_fq = json.loads(class_fq)
        df_fq = pd.DataFrame(class_fq.items(), columns=['Class', 'Number'])
        
        # Updating Inference results
        get_system_stat(stframe1, stframe2, stframe3, fps, df_fq)
