from utils.content_maker import ContentGenerator
from utils.video_maker import VideoGenerator
import utils.file as f
from utils.voice_maker import VoiceGenerator


if __name__ == "__main__":
  # url = 'https://vtv.vn/kinh-te/cham-dut-hoat-dong-huy-dong-tien-tu-tai-khoan-chung-khoan-20231221231114168.htm'
  # fileName = ContentGenerator.getContent(url)

  # print('FileName', fileName)

  fileName = 'katy-perry-chinh-phuc-khan-gia-viet-bang-loat-hit-o-le-trao-giai-vinfuture'

  # VideoGenerator.combineMp4Video([f.getPath(
  #     (fileName, fileName + '.mp4')), f.getPath(('video.mp4',))])

  fileData = f.readFile(f.getPath((fileName, fileName + '.json')))

  content = ''.join(fileData["texts"])
  # VideoGenerator.generateSubtitle(
  #     content, 139).write_videofile('ahihi.mp4', fps=24)
  images = f.downloadMultipleFiles(fileData["images"], folder=(fileName))

  # # print('Content', content)
  # # print('Images', images)

  audioPath = VoiceGenerator.getVoice(payload=content, fileName=fileName)

  VideoGenerator.generateVideo(
      audio=audioPath, images=images, videoName=f.getPath((fileName, f'{fileName}.mp4')), texts=content, textNote=fileName)
