import moviepy.editor as mp


def generateVideo(audio, images, videoName='video.mp4'):
  # Import the audio(Insert to location of your audio instead of audioClip.mp3)
  audioFile = mp.AudioFileClip(audio)
  # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
  imageFiles = list(map(lambda image: mp.ImageClip(
      image).set_duration(audioFile.duration/len(images)), images))

  clip = mp.concatenate_videoclips(imageFiles, method='compose')

  # Set the audio of the clip
  clip = clip.set_audio(audioFile)
  # Export the clip
  clip.write_videofile(videoName, fps=24)
