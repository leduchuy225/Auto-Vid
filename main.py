from models.data_model import DataModel
from utils.content_maker import ContentGenerator
from utils.image_process import ImageProcess
from utils.video_maker import VideoGenerator
import utils.file as f
from utils.voice_maker import VoiceGenerator


if __name__ == "__main__":
  # url = 'https://vtv.vn/'
  # url = 'https://vtv.vn/cong-nghe/nam-2023-xe-dien-dac-biet-thu-hut-nguoi-tieu-dung-toan-cau-20231226110405232.htm'
  # fileName = ContentGenerator.getContent(url)

  # print('FileName', fileName)

  fileName = 'asiancuptruyenthongindonesiabatngokhenngoidtvietnam'

  fileData: DataModel = DataModel.fromFileName(fileName, '2023-12-26')

  content = ContentGenerator.joinContent(fileData)
  images = f.downloadMultipleFiles(
      fileData.images, folder=('2023-12-26', fileName))

  images = ImageProcess.preProcess(images, (9, 16))

  # audioPath = VoiceGenerator.getVoice(payload=content, fileName=fileName)
  # print('Audio Path', audioPath)

  # VideoGenerator.generateVideo(
  #     audio=audioPath, images=images,
  #     videoName=f.getPath((fileName, f'{fileName}.mp4')),
  #     texts=content, header=fileData.catagory
  # )
