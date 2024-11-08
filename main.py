import streamlit as st
import pygame
import os

# Khởi tạo pygame mixer
pygame.mixer.init()

# Đường dẫn thư mục Sound
sound_dir = "Sounds/"

# Đường dẫn đến các bài nhạc
music_files = {
    0: os.path.join(sound_dir, "0. Công chúa bong bóng.mp3"),
    1: os.path.join(sound_dir, "1. Vui là con gái.mp3"),
    2: os.path.join(sound_dir, "2. Bạch Tuyết catwalk.mp3"),
    3: os.path.join(sound_dir, "3. Hòn tử đi ra.mp3"),
    4: os.path.join(sound_dir, "4. Đã làm gì đâu, đã chạm vào đâu.mp3"),
    5: os.path.join(sound_dir, "5. Nhạc tình cảm.mp3"),
    6: os.path.join(sound_dir, "6. Ánh mắt ta chạm nhau.mp3"),
    7: os.path.join(sound_dir, "7. Nhạc tiktok cute trend.mp3"),
    8: os.path.join(sound_dir, "8. Phép thuật Winx.mp3"),
    9: os.path.join(sound_dir, "9. Nhạc tịnh tâm.mp3"),
    10: os.path.join(sound_dir, "10. End.mp3"),
}

st.title("Music Player")

# Lưu trạng thái nhạc đang phát
if "playing_track" not in st.session_state:
    st.session_state.playing_track = None

# Hàm kiểm tra và phát/tắt nhạc
def toggle_music(track_id):
    if st.session_state.playing_track == track_id:  # Nếu bài này đang phát
        pygame.mixer.music.stop()  # Dừng nhạc
        st.session_state.playing_track = None
    else:  # Nếu không có nhạc nào hoặc nhạc khác đang phát
        pygame.mixer.music.stop()  # Dừng nhạc hiện tại (nếu có)
        pygame.mixer.music.load(music_files[track_id])  # Tải bài mới
        pygame.mixer.music.play()  # Phát bài
        st.session_state.playing_track = track_id

# Tạo hai cột
col1, col2 = st.columns([1, 1])  # Bên trái rộng hơn bên phải

# Cột bên trái: Các nút phát nhạc
with col1:
    for i in range(len(music_files)):
        if st.button(f"{i}: {os.path.basename(music_files[i])}"):
            toggle_music(i)

# Cột bên phải: Hiển thị thông tin nhạc đang phát
with col2:
    st.subheader("Now Playing")
    if st.session_state.playing_track is not None:
        st.info(f"{os.path.basename(music_files[st.session_state.playing_track])}")
    else:
        st.info("No music is playing.")
