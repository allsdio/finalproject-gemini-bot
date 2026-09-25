import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="EduData Bot",
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

# API Key
api_key = st.secrets["GEMINI_API_KEY"]

# Riwayat percakapan untuk tampilan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input pengguna
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
                client = genai.Client(api_key=api_key)

                system_instruction = f"""
                Anda adalah EduData Bot, seorang pakar Data Science dan AI Mentor.

                Bantu pengguna memahami Data Science, Python,
                Machine Learning, SQL, dan Data Analytics.

                Gaya bahasa: {tone}.

                Jawablah dengan jelas, terstruktur,
                dan mudah dipahami.
                """

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=temperature,
                        system_instruction=system_instruction
                    )
                )

                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                client.close()

            except Exception as e:
                st.error(f"Terjadi error: {e}")
