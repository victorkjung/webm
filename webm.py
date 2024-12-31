import streamlit as st
import os
import subprocess

# Setup directories
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Streamlit UI
st.title("WebM to MP3/WAV Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a WebM file", type=["webm"])

# Output format selection
output_format = st.selectbox("Select Output Format", ["mp3", "wav"])

# Convert button
if st.button("Convert"):
    if uploaded_file is not None:
        # Save uploaded file
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Generate output file path
        base_filename = os.path.splitext(uploaded_file.name)[0]
        output_path = os.path.join(CONVERTED_FOLDER, f"{base_filename}.{output_format}")

        # Debug: Print paths
        st.write(f"Input file path: {input_path}")
        st.write(f"Output file path: {output_path}")

        # FFmpeg command to convert
        command = ["ffmpeg", "-i", input_path, output_path]

        try:
            # Execute FFmpeg command
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            
            # If successful, show success message and download button
            st.success("Conversion successful!")
            with open(output_path, "rb") as file:
                st.download_button(
                    label="Download Converted File",
                    data=file,
                    file_name=f"{base_filename}.{output_format}",
                    mime=f"audio/{output_format}",
                )
        
        except subprocess.CalledProcessError as e:
            # If error occurs during conversion, display the error details
            st.error(f"Conversion failed! Error: {e.stderr.decode()}")
            st.write(f"FFmpeg stdout: {e.stdout.decode()}")
            st.write(f"FFmpeg stderr: {e.stderr.decode()}")

    else:
        st.warning("Please upload a file first.")
