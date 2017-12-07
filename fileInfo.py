import sys 
import os
import hashlib 
from pathlib import Path


def getName(path):
	name = os.path.basename(path)
	return name

def getSize(file):
	size = os.path.getSize(file)

def getSHA1(data):
	content = Path(data).read_text()
	SHA1Hash = hashlib.sha1()
	SHA1Hash.update(content.encode())
	return SHA1Hash.hexdigest()

def getMD5(data):
  	content = Path(data).read_text()
  	MD5hash = hashlib.md5()
  	MD5hash.update(content.encode())
  	return MD5hash.hexdigest()
