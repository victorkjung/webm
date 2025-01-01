#!/bin/bash
# Install FFmpeg on Streamlit Cloud

echo "Installing FFmpeg..."
apt-get update
apt-get install -y ffmpeg
echo "FFmpeg installation complete!"
