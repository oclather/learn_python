#coding=gbk

import time
import urllib	
import re

#使用时间戳生成文件名
def filename ():
	return int(time.time()*10%1000000)


def getHtmlContent(url):
	f = urllib.urlopen(url)
	content = f.read()
	f.close()
	return content


#http://www.baidu.com/img/bd_logo1.png
#保存图片
def getImage(url):
	data = getHtmlContent(url)
	image_file = open('./' + str (filename())+'.png','rw')
	image_file.write(data)
	image_file.close()	


def openFile(path,key):
	file = open(path,'r')
	data = file.read()
	result = re.findall(key,data)
	return result


def getImageUrl(url,key):
	data = getHtmlContent(url)
	result = re.findall(key,data)
	for i in result:
		print i
		#getImage(i)

def getImage2(url,filename):
	urllib.urlretrieve(url.filename)

getImageUrl('http://www.baidu.com','http:/.*?.png')


#getImage("http://s1.bdstatic.com/r/www/cache/static/home/img/icons_0c37e9b.png")

print getHtmlContent('http://s1.bdstatic.com/r/www/cache/static/global/img/quickdelete_33e3eb8.png')
getImage2("http://s1.bdstatic.com/r/www/cache/static/global/img/quickdelete_33e3eb8.png",str(filename())