import sys 
import os
import hashlib 



def main(argv):
	if argv[0] is None:
		file = '../data/mydata.txt'
	else:
		file = argv[1]
	
	print(getName(file))
	print(getSize(file))
	print(getSHA1(file))
	print(getMD5(file))

def getName(path):
	name = os.path.basename(path)
	return name

def getSize(path): # consistancy with above
	size = os.path.getsize(path)
	return size

def getSHA1(data):
	with open(data, "r+") as infile:		
		content = infile.readline()
	SHA1Hash = hashlib.sha1()
	SHA1Hash.update(content.encode())
	return SHA1Hash.hexdigest()

def getMD5(data):
	with open(data, "r+") as infile:		
		content = infile.readline()
  	MD5hash = hashlib.md5()
  	MD5hash.update(content.encode())
  	return MD5hash.hexdigest()


if __name__ == '__main__':
	main(sys.argv)
