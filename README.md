# Song Player 🎵

A simple Streamlit web application for playing audio files from the "Incomplete Module Style Guide" collection.

## Features

- 🎵 Play MP3 and WAV audio files
- 📱 Simple, clean interface
- 🔄 Easy song selection
- 📊 File size display

## Files

This app plays 7 audio files:
- Incomplete module style guide v1.mp3
- Incomplete module style guide v2.mp3
- Incomplete module style guide v3.mp3
- Incomplete module style guide v4.wav
- Incomplete module style guide v5.wav
- Incomplete module style guide v6.wav
- Incomplete module style guide v7.wav

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to `http://localhost:8501`

## Deployment on Render

1. Push this repository to GitHub
2. Connect your GitHub repository to Render
3. Render will automatically detect the `render.yaml` configuration
4. Your app will be deployed and accessible via the provided URL

## Tech Stack

- **Streamlit**: Web framework for the audio player interface
- **Python**: Backend logic
- **Render**: Hosting platform
