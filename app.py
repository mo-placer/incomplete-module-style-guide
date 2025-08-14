import streamlit as st
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Song Player",
    page_icon="🎵",
    layout="centered"
)

# App title
st.title("Song Player")
st.markdown("### Incomplete Module Style Guide")

# Get all audio files
audio_files = []
supported_formats = ['.mp3', '.wav']

for file in os.listdir('.'):
    if any(file.lower().endswith(fmt) for fmt in supported_formats):
        audio_files.append(file)

# Sort files naturally
audio_files.sort()

if not audio_files:
    st.error("No audio files found in the directory!")
else:
    st.markdown(f"Found {len(audio_files)} songs:")
    
    # Create a selection box for songs
    selected_song = st.selectbox(
        "Choose a song to play:",
        audio_files,
        index=0
    )
    
    # Display current song info
    st.markdown(f"**Now Playing:** {selected_song}")
    
    # Audio player
    try:
        with open(selected_song, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3' if selected_song.endswith('.mp3') else 'audio/wav')
    except Exception as e:
        st.error(f"Error loading audio file: {e}")