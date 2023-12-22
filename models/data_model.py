import json
from typing import List


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
