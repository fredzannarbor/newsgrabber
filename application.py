import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz
from flask import *

application = Flask(__name__)

## This will basically extract any novel information or scoops from a story.
@application.route("/", methods=['GET', 'POST'])
def home(object=None):
	
	tmUrls = getTechmemeUrls.TechmemeUrls()
	
	scoop = getscoopz.GetScoopz()

	urls = tmUrls.getTechmemeUrls()

	scoops = scoop.getScoopz(urls)

	return render_template('hello.html')

if __name__ == '__main__':
	application.run()