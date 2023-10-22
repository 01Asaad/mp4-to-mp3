from moviepy.editor import AudioFileClip
import os
def convert(name) :
    audio_clip = AudioFileClip(name + ".mp4")
    audio_clip.write_audiofile(name + ".mp3")
    audio_clip.close()

if __name__ == "__main__" :
    count=0
    for i in [file for file in os.listdir() if file.endswith(".mp4")] :
        try :
            convert(i)
            count+=1
        except : print(f"Failed converting {i}")
    print(f"Done converting {str(count)} files")
