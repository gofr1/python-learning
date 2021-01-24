from gtts import gTTS

# save text as a sound in mp3 file
tts = gTTS('hello')
tts.save('hello.mp3')