#!/usr/bin/env python3
import pytube

link = 'https://www.youtube.com/watch?v=FvE1oTRUMN4'
yt = pytube.YouTube(link)

best_audio_stream = yt.streams.filter(type='audio').order_by('abr').desc().first()

best_audio_stream.download('../../Downloads')

print(yt.metadata)
print(yt.description)
print(yt.vid_info_url)