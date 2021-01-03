#!/usr/bin/env python3

# sudo pip3 install pytube
import pytube

link = 'https://www.youtube.com/watch?v=jofNR_WkoCE'
yt = pytube.YouTube(link)

# available video streams
yt.streams

# take the first with the highest resolution
videos = yt.streams.order_by('resolution').desc().first()

# download
videos.download('../../Downloads')