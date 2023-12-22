import requests
from bs4 import BeautifulSoup
from models.data_model import DataModel
from utils.file import saveFile
from utils.utils import remove_accents


class ContentGenerator:
  # def getType(x):
  #   if x.name == 'p':
  #     return 'p'
  #   if x.name == 'div' and x.attrs['type'] == 'Photo':
  #     return 'photo'
  #   return 'others'

  def getContent(url: str):
    return ContentGenerator.getContentFromVTVNews(url)

  def handleText(text: str):
    return text.replace('\"', '').replace(u'\xa0', u' ')

  def getContentFromVTVNews(url: str):
    response = requests.request('GET', url)

    soup = BeautifulSoup(response.content)

    catagory = soup.select_one('div.adm-mainsection p.tenmuc').text

    content = soup.select_one('div.adm-mainsection div.noidung')

    title = content.select_one('h1.title_detail').text

    author = content.select_one('p.author').text

    entryBody = content.select_one('#entry-body')

    texts = list(map(lambda x: ContentGenerator.handleText(
        x.text), entryBody.select('p')))

    images = list(map(lambda x: x.attrs['src'], entryBody.select('img')))

    fileName = remove_accents(title.replace(' ', '-').lower())

    data = DataModel(id=fileName, url=url, catagory=catagory, images=images,
                     author=author, texts=texts, title=title)

    saveFile(data.toJson(), name=(fileName, fileName + '.json'))

    return fileName
