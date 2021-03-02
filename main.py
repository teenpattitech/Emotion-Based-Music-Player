import streamlit as st
import time

st.title("Welcome to Emotion-based music player")

nav = st.sidebar.radio("Navigation", ["Home", "About EMP", "Play EMP"])

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
manually as per the preference of the user
              <br />
              These are what they really
offer to users, so starting by studying Emotions and the construction of
these emotions, and developing the algorithm that can help me solve this
problem is the main focus and the main problem, and as I said before this
is a really hard and tough problem but in simple way it is already solved
Starting by design a very simple app that is easy to use, this the first step
Starting by building the back end of the functionality of the app by
building a Local Binary Pattern Histogram Neural Network to classify
the images, to try getting the most out of this algorithm and get accuracy
rate that can tell that the app has solved the problem And then to design
a very simple app that is easy to use and friendly These are the main
points of the problem statement of this project
              <br />
             """, True)
    st.markdown("### New Visitor?")
    if st.button("Register"):
        first, last = st.beta_columns(2)
        first.text_input("First Name")
        last.text_input("Last Name")
        email, mobile = st.beta_columns([3, 1])
        email.text_input("Email Id")
        mobile.text_input("Mobile No")
        username, pw, rpw = st.beta_columns(3)
        username.text_input("Username")
        pw.text_input("Password", type="password")
        rpw.text_input("Re-enter Password", type="password")
        check, space, submit = st.beta_columns(3)
        check.checkbox("I agree to all T&C", value=False)
        submit.button("Submit")

    st.markdown("### Already a visitor?")
    if st.button("Login", key="login"):
        email = st.text_input("Enter Email Id")
        password = st.text_input("Enter password", type="password")
        st.button("Login Here", key="entry")
    st.image("image-emo.jpg")


if nav == "About EMP":
    st.markdown("## EMP - Emotion-based Music Player")
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
    st.image("image-about-us.jpg")


if nav == "Play EMP":
    st.markdown("# Hi, I am your _buddy EMP_")
    st.markdown("## Click here to activate me")
    if(st.button("Activate EMP")):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        st.balloons()
        # st.markdown("""<hr>""", True)
        st.markdown("## Feel the music :sunglasses:")
        st.image("dynamite-image.jpg")
        st.audio("Dynamite-song.mp3")
        st.markdown("""<hr>""", True)
        st.image("drag-me-down-image.png")
        st.audio("DragMeDown-song.mp3")
