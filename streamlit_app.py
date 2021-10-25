import streamlit as st
from transformers import pipeline

st.image('https://tyche.club/wp-content/uploads/2015/10/tyche_main01_3.jpg')
st.title('AI Multitool')
st.success('Congratulations! You explore the AI World. 🤗🤗🤗😇😇😇')
st.balloons()
st.write('This app gives you an option to dive deeper in the World of AI. With 2 simple models you can see how much we can do.😎😎😎😎😎😎' )
st.write('Please take your time and sit with a cup of tea to explore the World of AI. ☕☕☕☕☕')

st.subheader('Please choose an option from list below \u2193')
option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Przetłumacz z angielskiego na niemiecki"
    ],
)

text = st.text_area(label="Wpisz tekst")
if option == "Wydźwięk emocjonalny tekstu (eng)":
    classifier = pipeline("sentiment-analysis")
if option == "Przetłumacz z angielskiego na niemiecki":
    classifier = pipeline("translation_en_to_de")

with st.spinner("Waiting for a result..."):
    answer = classifier(text)
    st.write(answer)

st.write("Index number: s18345")