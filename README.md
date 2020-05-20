# Flask YouTube Audio Downloader

This is a simple web gui for youtube-dl that is designed to be self-hosted using [Docker](https://www.docker.com/). The key point of this project is to be simple enough to manually review in minutes (so even beginners can see what it's doing) while also providing a solid foundation for future features should anyone decide to add them.

This app is meant to do one thing well: download the audio of a YouTube video as a `m4a` file through the browser given a YouTube link.

There are no settings to configure. All source files are less than 50 lines long at the time of writing this.

The number of dependencies have been minimized to make maintainability easy:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [ffmpeg](https://ffmpeg.org/)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl/)
- [Python 3.8+ (ideally)](https://www.python.org/); though this should work on Python 3.5+

## Running This Project

To run this locally for dev purposes:
```bash
# you must have the packages listed in requirements.txt; python must be v3.5+
python app.py
```

For Docker stuff, there's a handy `Makefile` included with the following commands:
- `make build`: builds the production-ready Docker image for this app
- `make up`: runs docker-compose to start up app container; image must already be built
- `make down`: shuts down and removes app container
- `make logs`: prints logs from app container
- `make shell`: opens bash shell into app container; app files are in /app; use ctrl-D to exit

## Cool Related Projects

- [YoutubeDL-Material](https://github.com/Tzahi12345/YoutubeDL-Material)
- [Invidious](https://github.com/omarroth/invidious)
- [youtube-dl-server](https://github.com/manbearwiz/youtube-dl-server)
