import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip


class VideoGenerator:
  def generateVideo(audio, images, texts: str, videoName='video.mp4'):
    # Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audioFile = mp.AudioFileClip(audio)
    # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)

    durationTime = audioFile.duration/len(images)

    imageFiles = [mp.ImageClip(m).set_duration(durationTime) for m in images]

    clip = mp.concatenate_videoclips(imageFiles, method='compose')

    # Set the audio of the clip
    clip = clip.set_audio(audioFile)

    if texts != None:
      pass

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

  def combineMp4Video(videos: list,  videoName='video_combine.mp4'):
    fileVideos = [mp.VideoFileClip(video) for video in videos]
    finalVideo = mp.concatenate_videoclips(fileVideos, method='compose')
    finalVideo.write_videofile(videoName, fps=24)

  def generateSubtitle(texts: str, duration: float):
    countWord = 0
    textSplitByDot = [text.strip()
                      for text in texts.replace('...', '.').split('.')]
    for sentence in textSplitByDot:
      print(sentence)
      print(len(sentence.split(' ')))

      countWord += len(sentence.split(' '))

    print(countWord)


# Xuất hiện trên sân khấu lễ trao giải VinFuture, Katy Perry đã trình diễn hai bài hát gắn liền với tên tuổi của cô là Unconditionally và Roar
# 28
# Đây là hai ca khúc đã từng thu hút hàng tỷ lượt người xem trên Youtube
# 16
# Với hai bản hit này, ca sĩ muốn truyền thông điệp về tinh thần, ý chí mạnh mẽ của phái nữ và tình yêu vô điều kiện với đam mê khoa học, sáng tạo
# 34

# 1
# Katy Perry trình diễn hai ca khúc Unconditionally và RoarKết thúc lễ trao giải, cô thể hiện bản hit Firework trong hiệu ứng sắc màu pháo hoa rực rỡ
# 29
# Katy Perry chinh phục khán giả Việt bằng loạt hit ở lễ trao giải VinFutureChia sẻ với báo giới, Katy Perry cho biết, trình diễn ở lễ trao giải VinFuture với cô là một cơ hội tuyệt vời
# 38
# Tôi chưa bao giờ hát ở Việt Nam trong các lần trước đây nhưng cuối cùng tôi đã làm được và hôm nay trong buổi trao giải thưởng VinFuture
# 29
# Đây là một cơ hội thật tuyệt vời, giải thưởng này tôn vinh những con người tuyệt vời đang thay đổi thế giới của chúng ta và đảm bảo thế giới của chúng ta an toàn và bền vững cho các thế hệ tương lai, ngôi sao sinh năm 1984 chia sẻ
# 52
# Katy Perry toả sáng trên sân khấu Lễ trao giải VinFutureTrả lời câu hỏi về lần thứ ba tới Việt Nam, Katy Perry cho biết, lần này cô được chứng kiến nhiều điều hơn và cũng có điều kiện để hiểu rõ ơn sự thay đổi này
# 47
# Xung quanh tôi có rất nhiều người Việt, quản lý của tôi cũng là người Việt nên cô ấy đã dạy tôi rất nhiều điều về lịch sử
# 28
# Thật thú vị khi đến một quốc gia có nền văn hóa khác và choáng ngợp trước tất cả những điều đó, nữ ca sỹ cho biết
# 27
# Lễ trao giải VinFuture là lần thứ ba Katy Perry đến Việt Nam
# 13
# Trước đó, vào năm 2015, cô làm khách mời tại một diễn đàn ở TP Hồ Chí Minh
# 18
# Một năm sau, Perry đến Ninh Thuận trong vai trò đại sứ thiện chí của Quỹ Nhi đồng Liên Hợp Quốc UNICEF
# 22
# Katy Perry chào khán giả Việt NamKaty Perry sinh năm 1984, là nữ nghệ sĩ có đĩa hát bán chạy nhất lịch sử của hãng thu Capitol Records (Mỹ) và là một trong những nghệ sĩ bán đĩa nhạc chạy nhất mọi thời đại
# 44
# Cô đã đạt được tổng cộng 115 tỷ lượt phát trực tuyến cùng doanh số bán hơn 70 triệu album và 140 triệu bài hát trên toàn thế giới
# 29
# Katy Perry cũng là chủ nhân của nhiều bài hát tỷ view trên YouTube như Roar, Dark Horse, Firework, Hot n cold, Wide Awake, Last Friday Night
# 27
# Cô từng giành 4 kỷ lục Guinness thế giới, 5 giải Billboard, 5 giải thưởng Âm nhạc Mỹ
# 18
# * Mời quý độc giả theo dõi các chương trình đã phát sóng của Đài Truyền hình Việt Nam trên TV Online và VTVGo!
# 24
# 524
