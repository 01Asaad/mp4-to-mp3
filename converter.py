from moviepy.editor import AudioFileClip
def convert(name) :
    audio_clip = AudioFileClip(name + ".mp4")
    audio_clip.write_audiofile(name + ".mp3")
    audio_clip.close()