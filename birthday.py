


import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Happy Birthday Abdul Hadi",
    page_icon="🎂",
    layout="wide"
)


# ---------------- MUSIC ----------------
with open("birthday.mp3", "rb") as audio_file:
    audio_data = audio_file.read()

st.audio(audio_data, format="audio/mp3")


# =================================================
#                    DESIGN
# =================================================

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(
        circle at top,
        #44345c 0%,
        #211a2b 45%,
        #09080d 100%
    );
}


/* General text */
.stMarkdown {
    font-family:
        "Segoe Print",
        "Bradley Hand",
        "Comic Sans MS",
        cursive;
}


/* Opening */
.opening {
    text-align: center;
    color: #d9c5ff;
    font-size: 20px;
    letter-spacing: 4px;
    margin-top: 25px;
}


/* Birthday heading */
.birthday {
    text-align: center;
    color: white;
    font-size: 58px;
    font-weight: 800;
    margin-top: 15px;
}


/* Name */
.name {
    text-align: center;
    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 90px;
    font-weight: bold;

    color: #efd9ff;

    text-shadow:
        0 0 15px rgba(230,190,255,0.5),
        0 0 35px rgba(230,190,255,0.25);

    margin-bottom: 30px;
}


/* Wishes heading */
.wish-heading {
    text-align: center;
    color: #f0d7ff;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 38px;
    margin-top: 45px;
    margin-bottom: 25px;
}


/* Wish card */
.wish-card {
    max-width: 850px;
    margin: auto;

    background: rgba(255,255,255,0.07);

    border: 1px solid rgba(235,205,255,0.30);

    border-radius: 28px;

    padding: 35px;

    box-shadow:
        0 15px 50px rgba(0,0,0,0.40);
}


/* Wish text */
.wish-main {
    text-align: center;

    color: #f8efff;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 23px;

    line-height: 2;

}


/* Special wish */
.special-wish {
    text-align: center;

    color: #efd0ff;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 25px;

    font-weight: bold;

    margin-top: 20px;
}


/* Divider */
.divider {
    text-align: center;

    color: #d9b9ff;

    font-size: 20px;

    margin: 25px 0;
}


/* Final heading */
.final-heading {
    text-align: center;

    color: #efd4ff;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 34px;

    margin-top: 55px;
}


/* Small wish boxes */
.small-wish {
    text-align: center;

    color: #f5edf9;

    font-family:
        "Segoe Print",
        "Bradley Hand",
        cursive;

    font-size: 20px;

    line-height: 1.8;
}


/* Footer */
.footer {
    text-align: center;

    color: #cbb4d9;

    font-size: 18px;

    margin-top: 45px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# =================================================
#                 OPENING
# =================================================

st.markdown(
    '<div class="opening">✨ A SPECIAL DAY • A SPECIAL PERSON ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="birthday">🎂 HAPPY BIRTHDAY 🎂</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="name">Abdul Hadi</div>',
    unsafe_allow_html=True
)


# ---------------- BALLOONS ----------------

st.balloons()


# =================================================
#                 SPECIAL WISHES
# =================================================

st.markdown(
    '<div class="wish-heading">💌 Special Wishes For You 💌</div>',
    unsafe_allow_html=True
)


# Native Streamlit card
with st.container(border=True):

    st.markdown(
        """
        <div class="wish-main">

        Today is not just another day... ✨

        <br>

        It's a beautiful day to celebrate
        someone truly special. 💫

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">♡ ───────── ✦ ───────── ♡</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="wish-main">

        May this new chapter of your life
        bring you happiness, success,
        peace and countless beautiful memories. 🌸

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">✨ ✨ ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="special-wish">

        🎉 Wishing you a beautiful
        and unforgettable birthday! 🎂

        </div>
        """,
        unsafe_allow_html=True
    )


# =================================================
#                 MEMORIES
# =================================================

st.markdown(
    '<div class="wish-heading">📸 Beautiful Memories 📸</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:
    st.image("images/image1.jpeg.jpeg")


with col2:
    st.image("images/image2.jpeg.jpeg")


with col3:
    st.image("images/image3.jpeg.jpeg")


# =================================================
#              FINAL WISHES
# =================================================

st.markdown(
    '<div class="final-heading">🌸 From The Heart 🌸</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

    st.markdown(
        '<div class="small-wish">✨ May your smile always stay bright. ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">♡</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-wish">🎈 May your dreams keep getting bigger and brighter. 🎈</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">♡</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-wish">🌸 May happiness follow you wherever you go. 🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider">♡</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-wish">🎂 May every birthday be more beautiful than the last. 🎂</div>',
        unsafe_allow_html=True
    )


# =================================================
#                  FOOTER
# =================================================

st.markdown(
    '<div class="footer">✨ Made with love & warm wishes ✨</div>',
    unsafe_allow_html=True
)