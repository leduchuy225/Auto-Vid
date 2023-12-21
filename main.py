from utils.content_maker import ContentGenerator
import utils.video_maker as vm
import utils.file as f
from utils.voice_maker import VoiceGenerator

url = 'https://vtv.vn/van-hoa-giai-tri/katy-perry-chinh-phuc-khan-gia-viet-bang-loat-hit-o-le-trao-giai-vinfuture-20231220223953313.htm'

if __name__ == "__main__":
  # fileName = ContentGenerator.getContent(url)
  fileName = 'katy-perry-chinh-phuc-khan-gia-viet-bang-loat-hit-o-le-trao-giai-vinfuture'
  fileData = f.readFile(f.getPath((fileName, fileName + '.json')))

  content = '\n'.join(fileData["texts"])
  images = f.downloadMultipleFiles(fileData["images"], folder=(fileName))

  print(content)
  print(images)
  # images = ['image.jpg', 'image2.jpg']
  # response = VoiceGenerator.getVoice(payload=content)

  # f.downloadFile(response["async"], name=f'{response["request_id"]}.mp3')
  # vm.generateVideo(audio=response["request_id"], images=images,)
