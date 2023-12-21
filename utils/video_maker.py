import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip


def generateVideo(audio, images, videoName='video.mp4'):
  # Import the audio(Insert to location of your audio instead of audioClip.mp3)
  audioFile = mp.AudioFileClip(audio)
  # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)

  durationTime = audioFile.duration/len(images)

  imageFiles = [mp.ImageClip(m).set_duration(durationTime) for m in images]

  clip = mp.concatenate_videoclips(imageFiles, method='compose')

  # Set the audio of the clip
  clip = clip.set_audio(audioFile)

  # def generator(txt): return mp.TextClip(
  #     txt, font='Arial', fontsize=24, color='white')

  # subs = [((0, 4), 'subs1'),
  #         ((4, 9), 'subs2'),
  #         ((9, 12), 'subs3'),
  #         ((12, 16), 'subs4')]

  # subtitles = SubtitlesClip(subs).set_pos(('center', 'bottom'))

  # clip = mp.CompositeVideoClip([clip, subtitles])

  # Export the clip
  clip.write_videofile(videoName, fps=24)
