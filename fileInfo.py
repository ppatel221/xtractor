import sys 
import os
import hashlib 
import md5

def getName(path):
	name = os.path.basename(path)
	return name

def getSize(file):
	size = os.path.getSize(file)

def getSHA1(data)
	SHA1Hash = hashlib.sha1()
	SHA1Hash = SHA1Hash.update(data)
	return SHA1Hash.hexdigest()

def getMD5(data)
	MD5Hash = md5.new()
	MD5Hash = MD5hash.update(data)
	return MD5hash.hexdigest()
