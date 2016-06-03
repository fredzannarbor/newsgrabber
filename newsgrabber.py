import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz

## This will basically extract any novel information or scoops from a story.

tmUrls = getTechmemeUrls.TechmemeUrls()
scoop = getscoopz.GetScoopz()

urls = tmUrls.getTechmemeUrls()

print(scoop.getScoopz(urls))