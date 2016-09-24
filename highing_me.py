#!/usr/bin/env python
#coding:utf8
import re
import urllib
import urllib2
import httplib
import time
import string




#获取页面源代码
def getHtml(url):
	try:
		#url="http://h5.highing.me/channel_details_list/5052"
		baidu_spider="Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
		headers={}
		headers['User-Agent']=baidu_spider

		#page = urllib2.Request(url,headers = headers)
		req = urllib2.Request(url,headers=headers)
		
		r=urllib2.urlopen(req)
		html=r.read()
		
		
		
		return html
	except httplib.BadStatusLine:
		pass
	
#获取图片内容并保存
def getImg(html):
	try:

    
		imgre = re.compile(r"src=\"((http://|https://|)[\w/\.\-/]*\.(jpg|png|gif))\"",re.I)
		imglist = re.findall(imgre,html)
		i = 0
		for imgurl in imglist:
			i = i + 1
			name = imgurl[-5:]
			filename=str(x)+str(i)+name[0][-4:]
			imurl=name[0]
			imurl = imurl.replace('/images/loading.gif','')
			#print imurl
			print filename
			if imurl is not '':
				urllib.urlretrieve(imurl, filename)
				#content = urllib.urlopen(str(name[0]).read()
				#open(r'tmp/' + str(filename),'w+').write(content)
	except httplib.BadStatusLine:
		pass

        
        
		
		
		

urls="http://h5.highing.me/channel_details_list/"

for x in range(5051,5057):
	allurl=urls+str(x)
	print allurl
	
	html = getHtml(allurl)
	getImg(html)
	time.sleep(5)
	


	
	


print 'done'