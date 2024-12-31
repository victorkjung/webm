# webm
Webm Conversion

### WebM to MP3/WAV Converter

This simple web application allows users to convert WebM audio files to either MP3 or WAV formats using **FFmpeg**. Built with Streamlit, it provides an intuitive interface for file uploading, format selection, and downloading the converted audio files.

#### Key Features:
- **File Upload**: Upload your WebM file directly from your local machine.
- **Format Selection**: Choose the output format between MP3 or WAV.
- **Conversion**: The app uses FFmpeg to process the conversion and provides real-time feedback.
- **Download**: Once the conversion is successful, download the converted file instantly.

#### How It Works:
1. Upload a WebM file.
2. Select whether you want the output in MP3 or WAV format.
3. Hit the "Convert" button and let the app process the conversion.
4. Download the converted file with just one click.

#### Requirements:
- **Python 3.x**
- **FFmpeg** installed and accessible from the command line.
- **Streamlit** library for the UI.

#### Setup & Run:
1. Clone the repository.
2. Install the necessary dependencies:
    ```bash
    pip install streamlit
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```

Once running, open the app in your browser and follow the instructions to upload and convert WebM files.

#### Notes:
- Ensure FFmpeg is installed on your machine and available in your system path.
- Works best with WebM files containing audio streams (audio-only WebM).

Feel free to contribute, report issues, or suggest improvements!
