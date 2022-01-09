from pytube import YouTube

link = input("Enter URL of Video")

stream = (YouTube(link)).streams.get_highest_resolution()

stream.download()