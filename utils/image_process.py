from PIL import Image


class ImageProcess:
  def handle_image(imagePath: str, ratio: tuple):
    im = Image.open(imagePath)
    x, y = im.size

    newHeight = int((x / ratio[0]) * ratio[1])
    newWidth = int((y / ratio[1]) * ratio[0])

    if newHeight > y:
      new_im = Image.new('RGB', (x, newHeight), 'black')
      new_im.paste(im, (0, int((newHeight-y)/2)))
      return new_im
    if newWidth > x:
      new_im = Image.new('RGB', (newWidth, y), 'black')
      new_im.paste(im, (int((newWidth-x)/2), 0))
      return new_im

    return im

  def preProcess(images: list[str], ratio: tuple):
    for image in images:
      im = ImageProcess.handle_image(image, ratio)
      im.save(image)

    return images
