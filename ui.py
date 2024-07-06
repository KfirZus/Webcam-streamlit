import cv2
import streamlit as st
from datetime import datetime

font = cv2.FONT_HERSHEY_COMPLEX

st.title("Motion Detector")
start = st.button("Start Camera")
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    close = st.button("Close Camera")
    while True:
        # Start the camera
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get current date and time
        date_time = (str(datetime.now().strftime('%A')) + "\n" + str(datetime.now().strftime("%H:%M:%S")))
        y0, dy = 50, 25
        for i, line in enumerate(date_time.split('\n')):
            y = y0 + i*dy
            cv2.putText(frame, line, (50, y), font, 0.60,
                        (128, 0, 128), 2, cv2.LINE_AA)
        streamlit_image.image(frame)
        if close:
            break
    camera.release()