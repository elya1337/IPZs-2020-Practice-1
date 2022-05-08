from pytube import YouTube
import locale
import re
import datetime
locale.setlocale(locale.LC_ALL, '')
def downloader(vid):
    output = ""
    for i, v in enumerate(vid.streams.filter(only_video=True, file_extension='mp4')):
        output += "viTag:" + str(v.itag) + " Video resolution: " + str(v.resolution) + " FPS: " + str(v.fps) + "\n"
    print(output)
address = input("Write the address : ")
video = YouTube(url=address)
print(f"\nVideo link:{video.watch_url}\n"
      f"video name: {video.title}\n"
      f"channel: {video.author}\n"
      f"views: {video.views:n}\n"
      f"video duration {str(datetime.timedelta(seconds=video.length))}\n")
downloader(video)
video.streams.get_by_itag(int(re.sub(r'\D', '', input("viTag: ")))).download(output_path='download/')
