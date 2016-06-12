import urllib2
from bs4 import BeautifulSoup
import requests
import re

class TechmemeUrls(object):

	def __init__(self):

		self.techmemeURLs = self.getTechmemeUrls()

	def getTechmemeUrls(self):

		## Get the headline and the URL for all top stories on Techmeme

		techmeme = urllib2.urlopen("http://techmeme.com/")
		read = techmeme.read()
		soup = BeautifulSoup(read, "html.parser")

		heds = soup.find_all(class_="L4")
		heds3 = soup.find_all(class_="L3")
		heds2 = soup.find_all(class_="L2")
		heds1 = soup.find_all(class_="L1")
		hedstr = ""
		urls = []
		
		for i in heds:
			url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(i))
			hedstr = re.sub(r'<[^>]*>', '', str(i))
			urls.append([hedstr,url[0]])
		for i in heds3:
			url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(i))
			hedstr = re.sub(r'<[^>]*>', '', str(i))
			urls.append([hedstr,url[0]])
		for i in heds2:
			url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(i))
			hedstr = re.sub(r'<[^>]*>', '', str(i))
			urls.append([hedstr,url[0]])
		for i in heds1:
			url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(i))
			hedstr = re.sub(r'<[^>]*>', '', str(i))
			if url == []:
				pass
			else:
			    urls.append([hedstr,url[0]])

		return(urls)