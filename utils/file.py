from genericpath import isfile
import json
import os
import requests
from pathlib import Path
from os.path import isfile, join


def getPath(name: tuple):
  return os.path.join(*(Path.cwd(), 'resources', *name))


def downloadFile(url: str, name: tuple):
  response = requests.request('GET', url)
  return saveFile(response.content, name, mode='wb')


def readFile(path: str):
  with open(path, 'r') as reader:
    return json.load(reader)


def saveFile(content, name: tuple, mode='w'):
  path = getPath(name[:len(name)-1])
  isExist = os.path.exists(path)

  if not isExist:
    os.makedirs(path)

  with open(getPath(name), mode=mode) as writer:
    writer.write(content)

  return getPath(name)


def getFileName(name: str):
  return name.split('/')[-1]


def getFileExtension(name: str):
  return '.' + name.split('.')[-1]


def downloadMultipleFiles(urls: list, folder: tuple):
  result = []
  for i in range(len(urls)):
    fileName = str(i) + getFileExtension(urls[i])
    fileDownload = downloadFile(url=urls[i], name=(folder, fileName))

    result.append(fileDownload)
  return result


def getExistFileType(folder: str, type: str):
  onlyfiles = [f for f in os.listdir(
      getPath((folder,))) if isfile(getPath((folder, f)))]
  for file in onlyfiles:
    if type in file:
      return getPath((folder, file))
  return None
