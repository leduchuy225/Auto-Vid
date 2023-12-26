from models.data_model import DataModel
from utils.content_maker import ContentGenerator
from utils.image_process import ImageProcess
from utils.video_maker import VideoGenerator
import utils.file as f
from utils.voice_maker import VoiceGenerator


if __name__ == "__main__":
  url = 'https://vtv.vn/the-gioi/mot-tuan-sau-dong-dat-o-trung-quoc-so-nguoi-chet-tang-len-149-hai-nguoi-van-mat-tich-20231225173001648.htm'
  fileName = ContentGenerator.getContent(url)

  print('FileName', fileName)

  fileData: DataModel = DataModel.fromFileName(fileName)

  content = ContentGenerator.joinContent(fileData)
  images = f.downloadMultipleFiles(fileData.images, folder=(fileName))

  images = ImageProcess.preProcess(images, (9, 16))

  audioPath = VoiceGenerator.getVoice(payload=content, fileName=fileName)
  print('Audio Path', audioPath)

  VideoGenerator.generateVideo(
      audio=audioPath, images=images,
      videoName=f.getPath((fileName, f'{fileName}.mp4')),
      texts=content, textNote=fileName
  )
