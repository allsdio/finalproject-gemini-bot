with st.chat_message("assistant"):
        with st.spinner("EduData Bot sedang berpikir..."):

            try:
                # Pastikan mengambil key langsung dengan fallback atau pastikan tidak kosong
                my_api_key = st.secrets.get("GEMINI_API_KEY", "")
                
                if not my_api_key:
                    st.error("API Key belum ditemukan di Streamlit Secrets!")
                
                client = genai.Client(api_key=my_api_key)

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

            except Exception as e:
                st.error(f"Terjadi error: {e}")
