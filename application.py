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
def home(URL=None):
    
    return render_template('hello.html')

@application.route("/grab", methods=['GET', 'POST'])
def grab(result=None):

	formdata['URL'] = request.form['URL']

	return render_template('grab.html', result=formdata['URL'])

if __name__ == '__main__':
	application.run()