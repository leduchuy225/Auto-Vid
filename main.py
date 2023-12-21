from utils.content_maker import ContentGenerator
import utils.video_maker as vm
import utils.file as f
from utils.voice_maker import VoiceGenerator

url = 'https://vtv.vn/van-hoa-giai-tri/katy-perry-chinh-phuc-khan-gia-viet-bang-loat-hit-o-le-trao-giai-vinfuture-20231220223953313.htm'

if __name__ == "__main__":
  fileName = ContentGenerator.getContent(url)

  print('FileName', fileName)

  fileData = f.readFile(f.getPath((fileName, fileName + '.json')))

  content = '\n'.join(fileData["texts"])
  images = f.downloadMultipleFiles(fileData["images"], folder=(fileName))

  # print('Content', content)
  # print('Images', images)

  audioPath = f.getExistFileType(fileName, 'mp3')
  if audioPath == None:
    print('Generate audio')
    response = VoiceGenerator.getVoice(payload=content)
    audioPathTuple = (fileName, f'{response["request_id"]}.mp3')
    audioPath = f.downloadFile(response["async"], name=audioPathTuple)

  vm.generateVideo(audioPath, images, f.getPath((fileName, f'{fileName}.mp4')))
