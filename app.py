import sys, os, shutil, time
from flask import Flask, render_template, request, send_file
import youtube_dl

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config['DOWNLOADS'] = os.path.join(app.root_path, 'tmp')

@app.route('/', methods=['GET', 'POST'])
def home():
    # clear downloads older than 5 minutes
    try:
        for file in os.listdir(app.config['DOWNLOADS']):
            filepath = os.path.join(app.config['DOWNLOADS'], file)
            if (time.time() - os.stat(filepath).st_ctime) > 300:
                if os.path.isfile(filepath):
                    os.remove(filepath)
    except Exception as e:
        print(e)

    if request.method == 'POST':
        ydl_opts = {
            'outtmpl': f'{app.config["DOWNLOADS"]}/%(title)s.%(ext)s',
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
            download_name = ydl.prepare_filename(info)
            download_name = download_name.split('.')
            download_name[-1] = 'm4a'
            download_name = '.'.join(download_name)

            ydl.download([url])

        return send_file(download_name, as_attachment=True)
    
    return render_template('home.html')


if __name__ == '__main__':
    try:
        shutil.rmtree('tmp', ignore_errors=True)
        os.mkdir('tmp')
    except Exception as e:
        print(e)
    app.run(debug=True, port=5000)
