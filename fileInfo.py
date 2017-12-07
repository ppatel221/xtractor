import sys 
import os
import hashlib 


def getName(path):
	name = os.path.basename(path)
	return name

def getSize(file):
	size = os.path.getSize(file)

def getSHA1(data):
	SHA1Hash = hashlib.sha1()
	SHA1Hash.update(data.encode())
	return SHA1Hash.hexdigest()

def getMD5(data):
  	MD5hash = hashlib.md5()
  	MD5hash.update(data.encode())
  	return MD5hash.hexdigest()
