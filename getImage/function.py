#coding=gbk

import time
import urllib

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
	image_file = open(str(filename())+'.png','w')
	image_file.write(data)
	image_file.close()	

print filename()

#getImage("http://www.baidu.com/img/bd_logo1.png")