import os, time
import youtube_dl
from pathlib import Path
from flask import Flask, render_template, request, send_file

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
downloads_dir = Path(app.root_path) / 'tmp'

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        # make the downloads directory if it does not already exist
        downloads_dir.mkdir(exist_ok=True)

        # clear downloads older than 5 minutes
        for filepath in downloads_dir.iterdir():
            if (time.time() - os.stat(filepath).st_ctime) > 300:
                filepath.unlink(missing_ok=True)
    except Exception as e:
        print('[Downloads Directory]', e)

    if request.method == 'POST':
        ydl_opts = {
            'outtmpl': f'{downloads_dir}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '192',
            }],
            'noplaylist': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            url = request.values.get('url')

            # get download name and change the extension from webm to m4a
            info = ydl.extract_info(url, download=False)
            download_name = Path(ydl.prepare_filename(info)).with_suffix('.m4a')

            ydl.download([url])

        return send_file(download_name, as_attachment=True)

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
