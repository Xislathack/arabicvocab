import streamlit as st
import random

def get_random_word():
    try:
        with open("vocabulary.txt", "r", encoding="utf-8") as file:
            words = file.read().splitlines()
            return random.choice(words)
    except FileNotFoundError:
        return "Vocabulary file not found. Please create vocabulary.txt"

st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic&display=swap" rel="stylesheet">
    </head>

    <style>
        body {
            font-family: 'Noto Naskh Arabic', serif;
        }
        /* You can add more CSS rules here to style other elements */
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("So'zlar")

if 'word' not in st.session_state:
    st.session_state.word = get_random_word()

if st.button("Keyingi so'z"):
    st.session_state.word = get_random_word()

st.write(f"## {st.session_state.word}")
