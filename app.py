import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key Gemini
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Setup Halaman Streamlit
st.set_page_config(
    page_title="EduData Bot - Asisten AI Data Science",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 EduData Bot")
st.caption("Asisten AI Interaktif untuk Belajar Data Science & Analytics")

# Sidebar Konfigurasi Parameter
st.sidebar.header("⚙️ Konfigurasi Parameter")
tone = st.sidebar.selectbox(
    "Gaya Bahasa (Tone):",
    ["Santai & Ramah", "Formal & Profesional", "Ringkas & Direct"],
    key="tone_select"
)
temperature = st.sidebar.slider("Kreativitas (Temperature):", 0.0, 1.0, 0.7, 0.1)

# Prompt Instruksi Sistem
system_instruction = f"""
Anda adalah EduData Bot, seorang pakar Data Science dan AI Mentor.
Tugas Anda adalah membantu pengguna memahami konsep Data Science, Python, Machine Learning, dan SQL.
Gaya bahasa respon Anda harus: {tone}.
Jawablah dengan terstruktur, berikan contoh kode jika relevan, dan dukung pengguna untuk terus belajar.
"""

# Inisialisasi Model Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={"temperature": temperature},
    system_instruction=system_instruction
)

# Inisialisasi Memory Chat di Session State
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Tampilkan Riwayat Percakapan
for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Input Pesan Pengguna

    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim ke Gemini dan dapatkan respon
    with st.chat_message("assistant"):
        with st.spinner("EduData Bot sedang berpikir..."):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)



api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Setup Halaman Streamlit
st.set_page_config(
    page_title="EduData Bot - Asisten AI Data Science",
    page_icon="🤖",
    layout="wide"
)


# Sidebar Konfigurasi Parameter
st.sidebar.header("⚙️ Konfigurasi Parameter")
tone = st.sidebar.selectbox("Gaya Bahasa (Tone):", ["Santai & Ramah", "Formal & Profesional", "Ringkas & Direct"])


# Prompt Instruksi Sistem
system_instruction = f"""
Anda adalah EduData Bot, seorang pakar Data Science dan AI Mentor.
Tugas Anda adalah membantu pengguna memahami konsep Data Science, Python, Machine Learning, dan SQL.
Gaya bahasa respon Anda harus: {tone}.
Jawablah dengan terstruktur, berikan contoh kode jika relevan, dan dukung pengguna untuk terus belajar.
"""

# Inisialisasi Model Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={"temperature": temperature},
    system_instruction=system_instruction
)

# Inisialisasi Memory Chat di Session State
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Tampilkan Riwayat Percakapan
for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Input Pesan Pengguna
if prompt := st.chat_input("Tanyakan sesuatu seputar Data Science...", key="chat_input"):
    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim ke Gemini dan dapatkan respon
    with st.chat_message("assistant"):
        with st.spinner("EduData Bot sedang berpikir..."):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
