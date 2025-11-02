import streamlit as st
from PIL import Image

st.set_page_config(page_title="🎬 Бесплатный ИИ-видео редактор", layout="centered")

st.markdown("""
<style>
    .stApp { max-width: 800px; margin: auto; background: #ffffff; }
    h1 { color: #1e40af; text-align: center; }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-size: 18px;
        padding: 14px;
        border-radius: 8px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎭 Генератор видео из фото")
st.markdown("Загрузите изображение и опишите движение — получите **реалистичное видео бесплатно** через Kling AI!")

uploaded_file = st.file_uploader("📸 Выберите изображение", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    motion = st.text_area("✍️ Опишите движение (на английском!)", height=100)
    if st.button("🚀 Перейти в Kling AI"):
        if motion.strip():
            st.success("✅ Готово! Следуйте инструкции:")
            st.markdown("1. Откройте [Kling AI](https://kling.ai)\n2. Загрузите это фото\n3. Вставьте текст:")
            st.code(motion)
            st.info("💡 Видео до 10 сек — бесплатно!")
        else:
            st.warning("Введите описание движения.")
else:
    st.info("ℹ️ Работает через бесплатный сервис [Kling AI](https://kling.ai)")
