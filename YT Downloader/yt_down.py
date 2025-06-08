import yt_dlp as yt
yt.YoutubeDL({"format": "best", "outtmpl": "%(title)s.%(ext)s"}).download(["https://www.youtube.com/watch?v=dQw4w9WgXcQ"])