import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import os
import queue
from os import listdir
from os.path import isfile, join
import time
from collections import Counter
from streamlit_webrtc import (
    WebRtcMode,
    webrtc_streamer,
)
capture_duration = 20
start_time = time.time()
emo = []
model = load_model('model1.h5')
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Neutral", 3: "Happy", 4: "Fearful", 5: "Sad", 6: "Surprised"}

def emotion_find():
    
    webrtc_ctx = webrtc_streamer(
            key="loopback",
            mode=WebRtcMode.SENDONLY,
            # client_settings=WEBRTC_CLIENT_SETTINGS,
        )
    st.markdown("## Click here to activate me")
    if(st.button("Activate EMP")):
        progress = st.progress(0)
        i=0
        while ( int(time.time() - start_time) < capture_duration and i<100):
            progress.progress(i+1)
            i=i+1
                # Find haar cascade to draw bounding box around face
            if webrtc_ctx.video_receiver:
                try:
                    video_frame = webrtc_ctx.video_receiver.get_frame(timeout=10)
                    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                    gray = cv2.cvtColor(video_frame.to_ndarray(format="bgr24"), cv2.COLOR_BGR2GRAY)
                    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

                    for (x, y, w, h) in faces:
                            #cv2.rectangle(video_frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
                        roi_gray = gray[y:y + h, x:x + w]
                        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                        prediction = model.predict(cropped_img)
                        maxindex = int(np.argmax(prediction))
                        emo.append(emotion_dict[maxindex])
                except queue.Empty:
                    time.sleep(0.1)
                    continue
        if not emo:
            st.markdown("## Face Not Detected. Try Again")
        else:
            def most_frequent(List):
                occurence_count = Counter(List)
                return occurence_count.most_common(1)[0][0]
            user_emotion = most_frequent(emo)
            st.markdown("## You are "+user_emotion)
            songs = [f for f in listdir("songs/"+user_emotion) if isfile(join("songs/"+user_emotion, f))]
            for song in songs:
                st.markdown(song)
                st.audio("songs/"+user_emotion+"/"+song)

st.title("Emotifyo")

nav = st.sidebar.radio("", ["Home", "About Emotify", "Our Team", "Play Emotify"])

if nav == "Home":
    st.markdown("""<br>""", True)
    st.markdown(""" Connecting
music and emotion in one single app is not applicable in
most areas because of complexity of the project and the implementation,
and even if they solved it in a research paper there is no app which is
applying this program, even the very well known apps Spotify, Anghami
and SoundCloud All of them are simple in the way of offering their
service, they offer the music itself with some features like pausing,
stopping, change the song back and front, shuffle, and creating playlists
manually as per the preference of the user.
              <br /><br />
              These are what they really
offer to users, so starting by studying Emotions and the construction of
these emotions, and developing the algorithm that can help me solve this
problem is the main focus and the main problem, and as I said before this
is a really hard and tough problem but in simple way it is already solved
Starting by design a very simple app that is easy to use.
              <br />
             """, True)
    st.image("images/image-emo.jpg")


if nav == "About Emotify":
    st.markdown("## _Emotify - Emotion-based Music Player_")
    st.markdown("""
      As
a music lover, I've always felt that music players should do far
more things than just playing songs and allowing users to create
play lists A music player should be intelligent and act according to
user's preferences A music player should help users organize and
play the songs automatically without putting much effort into
selection and re organization of songs The Emotion Based Music
Player provides a better platform to all the music listeners, and
ensures automation of song selection and periodic updating of
play lists This helps users organize and play songs based on their
moods The player should also give recommendation for users to
change songs on the go It calculates song weight based on LBPH to
help users have more customized and organized play lists""")
    st.image("images/image-about-us.jpg")

if nav == "Our Team":
    col1, col2, col3 = st.beta_columns(3)
    col1.markdown("### Warren Fernandes")
    col1.markdown("_\"Its Time to Roll\"_")
    col2.markdown("### Liny Mathew")
    col2.markdown("_\"Its Time to Rock\"_")
    col3.markdown("### Yash Deshmukh")
    col3.markdown("_\"Its Time for Shava Shava\"_")
    st.markdown("""<br>""", True)
    st.markdown("_\"~Your incharge of how you feel. Don't let anyone kill your vibe. Let your Emotion flow\"_", True)
    st.markdown("""<br>""", True)
    st.image("images/team.jpeg")

if nav == "Play Emotify":
    emotion_find()
    