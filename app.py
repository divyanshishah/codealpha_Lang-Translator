import streamlit as st
from deep_translator import MyMemoryTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

custom_css = """
<style>

/* Main background */
.stApp {
    background: #046f87;
    color: #b0840b;
}

/* Title and headings */
h1, h2, h3 {
    color: #FFFFFF !important;
}

/* Normal text */
p, label {
    color: #ccad72 !important;
}

/* Text input */
textarea {
    background-color: 	#b3ffec !important;
    color: #FFFFFF !important;
    border: 2px solid #7B1E5F !important;
    border-radius: 12px !important;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #2B1B2D !important;
    color: #FFFFFF !important;
    border: 2px solid #7B1E5F !important;
    border-radius: 12px !important;
}

/* Translate button */
.stButton > button {
    background-color: #7B1E5F !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

/* Button hover */
.stButton > button:hover {
    background-color: #A52A7A !important;
    color: #FFFFFF !important;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🌐 Language Translator")
st.write("Translate text across multiple languages using Python and Streamlit.")

# Dictionary mapping common language names to MyMemory locale codes
LANGUAGES = {
    "English": "en-US",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "German": "de-DE",
    "Italian": "it-IT",
    "Japanese": "ja-JP",
    "Chinese (Simplified)": "zh-CN",
    "Hindi": "hi-IN",
    "Arabic": "ar-SA",
    "Portuguese": "pt-PT",
    "Russian": "ru-RU",
    "Korean": "ko-KR"
}

# Source and Target Language Pickers
col1, col2 = st.columns(2)
with col1:
    source_lang_name = st.selectbox("From Language:", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang_name = st.selectbox("To Language:", list(LANGUAGES.keys()), index=1)

source_code = LANGUAGES[source_lang_name]
target_code = LANGUAGES[target_lang_name]

input_text = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

if st.button("Translate", type="primary"):
    if input_text.strip():
        try:
            # Explicitly pass valid source and target codes
            translated_text = MyMemoryTranslator(source=source_code, target=target_code).translate(input_text)
            
            st.subheader("Translation:")
            st.success(translated_text)
            
        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
    else:
        st.warning("Please enter some text before translating.")