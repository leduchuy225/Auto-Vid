import json
import requests
from bs4 import BeautifulSoup
from utils.file import saveFile
from utils.utils import remove_accents


class ContentGenerator:
  # def getType(x):
  #   if x.name == 'p':
  #     return 'p'
  #   if x.name == 'div' and x.attrs['type'] == 'Photo':
  #     return 'photo'
  #   return 'others'

  def handleText(text: str):
    return text.replace('\"', '').replace(u'\xa0', u' ')

  def getContent(url):
    response = requests.request('GET', url)

    soup = BeautifulSoup(response.content)

    jsonData = {}

    catagory = soup.select_one('div.adm-mainsection p.tenmuc').text
    jsonData["catagory"] = catagory

    content = soup.select_one('div.adm-mainsection div.noidung')

    title = content.select_one('h1.title_detail').text
    jsonData["title"] = title

    author = content.select_one('p.author').text
    jsonData["author"] = author

    entryBody = content.select_one('#entry-body')

    # orders = list(map(ContentGenerator.getType, entryBody))
    # jsonData['orders'] = orders

    texts = list(map(lambda x: ContentGenerator.handleText(
        x.text), entryBody.select('p')))
    jsonData['texts'] = texts

    images = list(map(lambda x: x.attrs['src'], entryBody.select('img')))
    jsonData['images'] = images

    fileName = remove_accents(title.replace(' ', '-').lower())
    saveFile(json.dumps(jsonData), name=(fileName, fileName + '.json'))

    return fileName
