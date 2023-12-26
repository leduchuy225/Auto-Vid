import requests
from bs4 import BeautifulSoup
from models.data_model import DataModel
from utils.file import saveFile
from utils.utils import remove_accents


class ContentGenerator:
  def getContent(url: str):
    return ContentGenerator.getContentFromVTVNews(url)

  def handleText(text: str):
    return text.replace('\"', '').replace(u'\xa0', u' ')

  def getName(data: str):
    return remove_accents(
        ''.join([i for i in data if i.isalpha()]).lower())

  def joinContent(fileData: DataModel):
    return fileData.title + '.' + ' '.join(fileData.texts)

  # def getContentFromVTVShortsNews(url: str):
  #   response = requests.request('GET', url)

  #   soup = BeautifulSoup(response.content, features="html.parser")
  #   pass

  def getContentFromVTVNews(url: str):
    response = requests.request('GET', url)

    soup = BeautifulSoup(response.content, features="html.parser")

    catagory = soup.select_one('div.adm-mainsection p.tenmuc').text

    content = soup.select_one('div.adm-mainsection div.noidung')

    title = content.select_one('h1.title_detail').text

    author = content.select_one('p.author').text

    entryBody = content.select_one('#entry-body')

    texts = list(map(lambda x: ContentGenerator.handleText(
        x.text), entryBody.select('p')))

    images = list(map(lambda x: x.attrs['src'], content.select('img')))

    fileName = ContentGenerator.getName(title)

    data = DataModel(id=fileName, url=url, catagory=catagory, images=images,
                     author=author, texts=texts, title=title)

    saveFile(data.toJson(), name=(fileName, fileName + '.json'))

    return fileName
