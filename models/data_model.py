import json
from typing import List
import utils.file as f


class DataModel:
  def __init__(self, id: str, url: str, catagory: str, title: str, author: str, texts: List[str], images: List[str]):
    self.id = id
    self.url = url,
    self.title = title
    self.texts = texts
    self.author = author
    self.images = images
    self.catagory = catagory

  def toJson(self):
    return json.dumps(self.__dict__)

  def fromJson(json):
    return DataModel(id=json["id"],
                     url=json["url"],
                     title=json["title"],
                     texts=json["texts"],
                     author=json["author"],
                     images=json["images"],
                     catagory=json["catagory"]
                     )

  def fromFileName(fileName: str):
    fileData = f.readFile(f.getPath((fileName, fileName + '.json')))
    return DataModel.fromJson(fileData)
