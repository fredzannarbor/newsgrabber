from flask import *
import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz
import cues
import getsoup
import getmetadata

app = Flask(__name__)
scoop = getscoopz.GetScoopz()
soup = getsoup.GetSoup()
metadata = getmetadata.GetMetadata()

@app.route("/", methods=['GET', 'POST'])

def home():
    
    return render_template('hello.html')

@app.route("/grab", methods=['GET', 'POST'])

def grab():

	formdata = {}
	url = request.form['link']
	scoops = scoop.getScoopz(url)
	formdata['publication'] = scoops[0]
	formdata['scoops'] = scoops[1]

	return render_template('grab.html', scoops=formdata)

@app.route("/techmeme", methods=['GET', 'POST'])

def techmeme():

	returnform = []

	tmUrls = getTechmemeUrls.TechmemeUrls()

	for i in tmUrls.techmemeURLs:

		# an_item = dict(headline=i[0], url=i[1])
		# returnform.append(an_item)

		result = scoop.getScoopz(i[1])
		an_item = dict(publication=result[0], headline=i[0], scoops=result[1])
		returnform.append(an_item)

	return render_template('techmeme.html', scoops=returnform)

if __name__ == '__main__':
	app.run()