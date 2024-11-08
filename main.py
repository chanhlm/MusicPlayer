import streamlit as st
import os

# Đường dẫn đến thư mục chứa các file âm thanh
sound_dir = "Sounds/"

st.set_page_config(page_title="Play Music", layout="wide")

# Lấy danh sách tất cả các file âm thanh trong thư mục Sound và sắp xếp
audio_files = sorted([f for f in os.listdir(sound_dir) if f.endswith(('.mp3', '.wav'))])


# Khởi tạo session state để lưu trạng thái phát/dừng của từng file
if "audio_states" not in st.session_state:
    st.session_state.audio_states = {audio: False for audio in audio_files}  # False: dừng, True: phát

# Hàm chuyển đổi trạng thái phát/tạm dừng của bài nhạc
def toggle_audio(audio_file):
    # Đảo trạng thái bài nhạc được chọn
    st.session_state.audio_states[audio_file] = not st.session_state.audio_states[audio_file]
    # Tắt tất cả các bài khác
    for other_audio in audio_files:
        if other_audio != audio_file:
            st.session_state.audio_states[other_audio] = False

# Tạo hai cột: Cột nút bấm và cột phát nhạc
col1, col2 = st.columns([1, 1])

# Cột bên trái: Danh sách nút bấm phát nhạc với STT
with col1:
    for index, audio_file in enumerate(audio_files, start=0): 
        if st.button(f"{index} - {audio_file}"):
            toggle_audio(audio_file)  # Chuyển đổi trạng thái phát/tạm dừng của bài nhạc

# Cột bên phải: Trình phát nhạc và thông tin bài nhạc
with col2:
    st.subheader("Now Playing 🎧")
    current_playing = [audio for audio, is_playing in st.session_state.audio_states.items() if is_playing]

    if current_playing:
        audio_file = current_playing[0]
        st.audio(os.path.join(sound_dir, audio_file), format="audio/mp3", start_time=0)
        st.info(f"Đang phát: **{audio_file}**")
    else:
        st.info("Không có âm thanh nào đang phát.")
