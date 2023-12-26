import os
from pathlib import Path
import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip


class VideoGenerator:
  def generateVideo(audio, images: list[str], texts: str, header: str,  videoName='video.mp4'):
    # Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audioFile = mp.AudioFileClip(audio)
    # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)

    if len(images) == 0:
      images.append(os.path.join(Path.cwd(), 'default.jpg'))

    durationTime = (audioFile.duration/len(images))
    imageFiles = [mp.ImageClip(m).set_duration(durationTime) for m in images]

    clip = mp.concatenate_videoclips(imageFiles, method='compose')

    print(clip.size)

    if texts != None:
      subtitleClip = SubtitlesClip(
          VideoGenerator.generateSubtitle(texts, audioFile.duration),
          lambda txt: mp.TextClip(txt, font='JetBrains-Mono-Regular',
                                  color='white', size=clip.size, method='caption', fontsize=26, align='South'),
      )
      clip = mp.CompositeVideoClip([clip, subtitleClip])

    if header != None:
      headerClip = mp.TextClip(header, font='JetBrains-Mono-Regular',
                               color='white', size=clip.size, fontsize=28, align='North').set_duration(audioFile.duration)
      clip = mp.CompositeVideoClip([clip, headerClip])

    clip = clip.set_audio(audioFile)
    clip.write_videofile(videoName, fps=24)

  def combineMp4Video(videos: list,  videoName='video_combine.mp4'):
    fileVideos = [mp.VideoFileClip(video) for video in videos]
    finalVideo = mp.concatenate_videoclips(fileVideos, method='compose')
    finalVideo.write_videofile(videoName, fps=24)

  def generateSubtitle(texts: str, duration: float):
    print(duration)

    countWord = 0
    subtitles = []
    currentTime = 0
    textSplitByDot = [text.strip()
                      for text in texts.replace('...', '.').split('.')]
    for sentence in textSplitByDot:
      countWord += len(sentence.split(' '))

    print(countWord)

    secondPerWord = duration / countWord

    print(secondPerWord)

    for sentence in textSplitByDot:
      if sentence.strip() == '':
        continue
      countWordPerSentence = len(sentence.split(' '))
      subtitles.append(
          ((currentTime, currentTime + secondPerWord * countWordPerSentence), sentence))
      currentTime += secondPerWord * countWordPerSentence

    print(subtitles)

    return subtitles
