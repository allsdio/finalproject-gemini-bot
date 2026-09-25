import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="EduData Bot - Asisten AI Data Science",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 EduData Bot")
st.caption("Asisten AI Interaktif untuk Belajar Data Science & Analytics")

# Sidebar
st.sidebar.header("⚙️ Konfigurasi Parameter")

tone = st.sidebar.selectbox(
    "Gaya Bahasa (Tone):",
    [
        "Santai & Ramah",
        "Formal & Profesional",
        "Ringkas & Direct"
    ]
)

temperature = st.sidebar.slider(
    "Kreativitas (Temperature):",
    0.0,
    1.0,
    0.7,
    0.1
)

# API Gemini
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# Instruksi AI
system_instruction = f"""
Anda adalah EduData Bot, seorang pakar Data Science dan AI Mentor.

Tugas Anda membantu pengguna memahami:
- Data Science
- Python
- Machine Learning
- SQL
- Data Analytics

Gaya bahasa respon: {tone}.

Jawablah dengan terstruktur, mudah dipahami,
dan berikan contoh kode jika relevan.
"""

# Menyimpan percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Membuat chat Gemini
chat = client.chats.create(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        temperature=temperature,
        system_instruction=system_instruction
    )
)
    st.session_state.ch
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=system_instruction
        )
    )

# Menampilkan percakapan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Tanyakan sesuatu seputar Data Science..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("EduData Bot sedang berpikir..."):
            try:
                response = st.session_state.chat.send_message(
                    message=prompt
                )

                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Terjadi error: {e}")
