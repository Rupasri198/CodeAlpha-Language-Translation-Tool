import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 AI Language Translator")
st.write("Translate text between different languages using AI-powered translation.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter text to translate",
    placeholder="Type your text here...",
    height=150
)

if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text first.")

    elif source_language == target_language:
        st.info("Source and target languages are the same.")
        st.write(text)

    else:
        try:
            translator = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translation = translator.translate(text)

            st.success("Translation completed!")

            st.subheader("Translated Text")
            st.text_area(
                "Result",
                translation,
                height=150
            )

        except Exception as e:
            st.error(
                "Translation failed. Please check your internet connection and try again."
            )
            st.write(e)

st.divider()

st.caption("CodeAlpha Artificial Intelligence Internship - Task 1")
