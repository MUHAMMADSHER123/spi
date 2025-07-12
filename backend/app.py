from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import yt_dlp
import os
import uuid
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_audio(url):
    # Har bir yuklab olish uchun noyob fayl nomi
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filepath,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Check if file was created successfully
        if os.path.exists(filepath):
            return filepath
        else:
            raise Exception("Audio file could not be downloaded")
            
    except Exception as e:
        # Clean up any partial files
        if os.path.exists(filepath):
            os.remove(filepath)
        raise e

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
        
        url = data['url'].strip()
        if not url:
            return jsonify({'error': 'URL cannot be empty'}), 400
        
        # Download the audio file
        filepath = download_audio(url)
        
        # Send the file
        response = send_file(
            filepath, 
            as_attachment=True,
            download_name="audio.mp3",
            mimetype='audio/mpeg'
        )
        
        # Clean up the file after sending
        @response.call_on_close
        def cleanup():
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
            except:
                pass
        
        return response
        
    except Exception as e:
        error_msg = str(e)
        if "Video unavailable" in error_msg:
            return jsonify({'error': 'Video not available or private'}), 400
        elif "Sign in" in error_msg:
            return jsonify({'error': 'This video requires authentication'}), 400
        elif "copyright" in error_msg.lower():
            return jsonify({'error': 'This content is protected by copyright'}), 400
        else:
            return jsonify({'error': f'Download failed: {error_msg}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 