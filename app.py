import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🎬 Бесплатный ИИ-видео редактор",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Кастомный стиль для красоты
st.markdown("""
<style>
    .stApp {
        max-width: 800px;
        margin: auto;
        background-color: #ffffff;
        padding: 20px;
    }
    h1 {
        color: #1e40af;
        text-align: center;
        font-size: 2.2em;
        margin-bottom: 10px;
    }
    .stMarkdown p, .stMarkdown li {
        font-size: 1.1em;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-size: 18px;
        padding: 14px 28px;
        border-radius: 10px;
        border: none;
        width: 100%;
        font-weight: 600;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    .uploadedImage {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.title("🎭 Генератор видео из фото")
st.markdown("Загрузите изображение и опишите движение — получите **реалистичное видео бесплатно** через Kling AI!")

# Загрузка файла
uploaded_file = st.file_uploader("📸 Выберите изображение (JPG/PNG)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ваше изображение", use_column_width=True, output_format="PNG")

    # Поле для текста движения
    motion = st.text_area(
        "✍️ Опишите движение (на английском!)",
        placeholder="Примеры:\n• The camera slowly zooms in on the face\n• The person turns head to the right and smiles\n• Leaves gently sway in the wind",
        height=120
    )

    # Кнопка
    if st.button("🚀 Перейти в Kling AI — получить видео бесплатно"):
        if not motion.strip():
            st.warning("⚠️ Пожалуйста, опишите движение.")
        else:
            st.success("✅ Всё готово! Следуйте инструкции ниже.")
            st.markdown("### 🔗 Как создать видео:")
            st.markdown("""
            1. **Откройте [Kling AI](https://kling.ai)** в новой вкладке  
               👉 [Нажмите здесь, чтобы открыть](https://kling.ai)
            2. Нажмите **«Image to Video»**
            3. **Загрузите это же изображение**
            4. Вставьте ваш текст движения:
            """)
            st.code(motion.strip(), language="text")
            st.markdown("""
            5. Нажмите **Generate** → подождите ~1 минуту → скачайте видео!
            """)
            st.info("💡 **Kling AI полностью бесплатен** (требуется регистрация через email или WeChat). Поддерживает видео до **10 секунд** в Full HD!")
else:
    st.info("ℹ️ Это приложение помогает быстро подготовить запрос для **Kling AI** — самого мощного бесплатного генератора видео на основе изображения и текста.")
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
