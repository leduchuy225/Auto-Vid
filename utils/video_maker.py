import moviepy.editor as mp
from moviepy.video.fx.resize import resize
from moviepy.video.tools.subtitles import SubtitlesClip


class VideoGenerator:
  def generateVideo(audio, images, texts: str, textNote: str,  videoName='video.mp4'):
    # Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audioFile = mp.AudioFileClip(audio)
    # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)

    clip = mp.ColorClip(size=(1080, 1920), duration=audioFile.duration)

    if len(images) > 0:
      durationTime = (audioFile.duration/len(images))
      imageFiles = [mp.ImageClip(m).set_duration(durationTime) for m in images]
      clip = mp.concatenate_videoclips(imageFiles, method='compose')

    if texts != None:
      subtitleClip = SubtitlesClip(
          VideoGenerator.generateSubtitle(texts, audioFile.duration),
          lambda txt: mp.TextClip(txt, font='SVN-Arial-Regular',
                                  color='white', size=clip.size, align='South', method='caption'),
      )
      clip = mp.CompositeVideoClip([clip, subtitleClip])

    # if textNote != None:
    #   textNoteClip = SubtitlesClip(
    #       [((0, audioFile.duration), textNote)]
    #   ).set_pos(('center'))
    #   clip = mp.CompositeVideoClip([clip, textNoteClip])

    # Set the audio of the clip
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
