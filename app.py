# Создаём папку
mkdir kling-app
cd kling-app

# Устанавливаем зависимости
pip install streamlit pillow

# Создаём файл app.py одной командой
echo import streamlit as st > app.py
echo from PIL import Image >> app.py
echo. >> app.py
echo st.set_page_config(page_title="🎬 Бесплатный ИИ-видео редактор", layout="centered") >> app.py
echo st.title("🎭 Генератор видео из фото") >> app.py
echo st.markdown("Загрузите изображение и опишите движение — получите видео через **Kling AI**!") >> app.py
echo. >> app.py
echo uploaded_file = st.file_uploader("📸 Выберите фото (JPG/PNG)", type=["jpg", "jpeg", "png"]) >> app.py
echo. >> app.py
echo if uploaded_file: >> app.py
echo     image = Image.open(uploaded_file) >> app.py
echo     st.image(image, use_column_width=True) >> app.py
echo     motion = st.text_area("✍️ Опишите движение (на английском!)", height=100) >> app.py
echo     if st.button("🚀 Перейти в Kling AI"): >> app.py
echo         if motion.strip(): >> app.py
echo             st.success("✅ Готово! Следуйте инструкции:") >> app.py
echo             st.markdown("1. Откройте [Kling AI](https://kling.ai)\\n2. Нажмите **Image to Video**\\n3. Загрузите это фото\\n4. Вставьте текст:") >> app.py
echo             st.code(motion) >> app.py
echo             st.info("💡 Видео до 10 сек — бесплатно!") >> app.py
echo         else: >> app.py
echo             st.warning("Пожалуйста, опишите движение.") >> app.py
echo else: >> app.py
echo     st.info("ℹ️ Это приложение помогает подготовить запрос для [Kling AI](https://kling.ai)") >> app.py
