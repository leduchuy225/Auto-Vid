import json
import os
import requests
from pathlib import Path


def getPath(name):
  return os.path.join(*(Path.cwd(), 'resources', *name))


def downloadFile(url: str, name: tuple):
  response = requests.request('GET', url)
  print(response.text)
  return saveFile(response.content, name)


def readFile(path: str):
  with open(path, 'r') as reader:
    return json.load(reader)


def saveFile(content: str, name: tuple):
  path = getPath(name[:len(name)-1])
  isExist = os.path.exists(path)

  if not isExist:
    os.makedirs(path)

  with open(getPath(name), 'w') as writer:
    writer.write(content)

  return getPath(name)


def getFileName(name: str):
  return name.split('/')[-1]


def downloadMultipleFiles(urls: list, folder: tuple):
  result = []
  for url in urls:
    result.append(downloadFile(url=url, name=(*folder, getFileName(url))))
  return result
