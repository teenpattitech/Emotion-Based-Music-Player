import streamlit as st
import time

st.title("Welcome to Emotion-based music player")

nav = st.sidebar.radio("Navigation", ["Home", "About EMP", "Play EMP"])

if nav == "Home":
    st.markdown("""<br>""", True)
    st.markdown(""" Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae
              earum quidem unde ad iure temporibus.
              <br />
              Voluptatum, eveniet. Quibusdam, quam esse rerum aspernatur aliquid
              perferendis veniam! Enim laborum mollitia in, officiis aliquam
              reprehenderit et sint vero.
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
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellat id harum rerum deserunt doloremque vel eligendi quia qui deleniti non tempore praesentium tenetur soluta ea quidem quae animi, vitae eveniet?  Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellat id harum rerum deserunt doloremque vel eligendi quia qui deleniti non tempore praesentium tenetur soluta ea quidem quae animi, vitae eveniet?""")
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
