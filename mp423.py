# from moviepy.editor import VideoFileClip,AudioFileClip
# mp4_file ="./music/3000 Miles.mp4"
# mp3_file="3000 Miles.mp3"
# audioclip = AudioFileClip(mp4_file)
# audioclip.write_audiofile(mp3_file)
# audioclip.close()
# audioclip.close()

import os
from moviepy.editor import VideoFileClip,AudioFileClip
 
# Get the list of all files and directories
path = "./music"
dir_list = os.listdir(path)

for i in range(0, len(dir_list)):
    mp4_file =f"./music/{dir_list[i]}"
    mp3_file=f"./mp3/{dir_list[i]}"
    audioclip = AudioFileClip(mp4_file)
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    audioclip.close()