import streamlit as st
import requests
import time
import tempfile
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# === Стиль: тёмный + фисташковый ===
st.markdown("""
<style>
    .stApp { background-color: #121212; color: #E0E0E0; }
    h1, h2, h3 { color: #A8D8B9 !important; }
    .stButton>button {
        background-color: #A8D8B9;
        color: #1A1A1A;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="🎬 Персонаж с твоим голосом", layout="centered")
st.title("🎭 ИИ-персонаж + Твой голос")
st.markdown("Загрузите фото и аудио — персонаж 'заговорит' вашим голосом!")

# === Секреты ===
RUNWAY_API_KEY = st.secrets.get("RUNWAY_API_KEY")
if not RUNWAY_API_KEY:
    st.error("⚠️ RUNWAY_API_KEY не настроен.")
    st.stop()

# === Загрузки ===
uploaded_image = st.file_uploader("📸 Фото персонажа", type=["jpg", "jpeg", "png"])
uploaded_audio = st.file_uploader("🎤 Ваше аудио (MP3/WAV)", type=["mp3", "wav"])

if uploaded_image and uploaded_audio:
    st.image(uploaded_image, caption="Персонаж", use_column_width=True)
    st.audio(uploaded_audio, format="audio/mp3")

    motion_prompt = st.text_input(
        "🎥 Движение (на англ.)",
        value="subtle head movement, natural breathing, slight blink",
        help="Рекомендуется: нейтральные движения"
    )

    if st.button("🎥 Создать видео", type="primary"):
        # === 1. Генерация видео через Runway ===
        with st.spinner("🔄 Генерация персонажа..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
                tmp_img.write(uploaded_image.getvalue())
                img_path = tmp_img.name

            upload_resp = requests.post(
                "https://api.runwayml.com/v1/upload",
                headers={"Authorization": f"Bearer {RUNWAY_API_KEY}"},
                files={"file": open(img_path, "rb")}
            )
            if upload_resp.status_code != 200:
                st.error("❌ Ошибка загрузки фото.")
                st.stop()
            asset_id = upload_resp.json()["id"]

            gen_resp = requests.post(
                "https://api.runwayml.com/v1/generations",
                headers={"Authorization": f"Bearer {RUNWAY_API_KEY}"},
                json={"model": "gen3-alpha", "prompt": motion_prompt, "image": asset_id}
            )
            if gen_resp.status_code != 201:
                st.error("❌ Ошибка генерации.")
                st.stop()

            gen_id = gen_resp.json()["id"]
            for _ in range(100):
                time.sleep(6)
                status = requests.get(
                    f"https://api.runwayml.com/v1/generations/{gen_id}",
                    headers={"Authorization": f"Bearer {RUNWAY_API_KEY}"}
                ).json()
                if status["status"] == "succeeded":
                    video_url = status["output"]["video"]
                    vid_data = requests.get(video_url).content
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_vid:
                        tmp_vid.write(vid_data)
                        video_path = tmp_vid.name
                    break
                elif status["status"] == "failed":
                    st.error("❌ Видео не создано.")
                    st.stop()
            else:
                st.error("⏰ Таймаут.")
                st.stop()

        # === 2. Замена аудио ===
        with st.spinner("🔊 Добавление вашего голоса..."):
            # Сохраняем аудио
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_aud:
                tmp_aud.write(uploaded_audio.getvalue())
                audio_path = tmp_aud.name

            # Склейка
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            # Обрезаем/растягиваем аудио под видео
            if audio_clip.duration > video_clip.duration:
                audio_clip = audio_clip.subclip(0, video_clip.duration)
            elif audio_clip.duration < video_clip.duration:
                # Повторяем аудио, если оно короче
                from moviepy.audio.fx import audio_loop
                audio_clip = audio_loop.audio_loop(audio_clip, duration=video_clip.duration)

            final_clip = video_clip.set_audio(audio_clip)
            with tempfile.NamedTemporaryFile(delete=False, suffix="_final.mp4") as tmp_out:
                final_clip.write_videofile(
                    tmp_out.name,
                    codec="libx264",
                    audio_codec="aac",
                    logger=None
                )
                final_path = tmp_out.name

        # === Результат ===
        st.success("✅ Видео готово! Персонаж говорит вашим голосом.")
        st.video(final_path)
        with open(final_path, "rb") as f:
            st.download_button(
                "📥 Скачать видео",
                f,
                file_name="talking_character.mp4",
                mime="video/mp4"
            )
else:
    st.info("ℹ️ Загрузите фото и аудио. Видео будет сгенерировано с вашим голосом!")
