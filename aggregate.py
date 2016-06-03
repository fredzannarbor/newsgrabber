import urllib2
from bs4 import BeautifulSoup
import requests
import re


Reporter = ""
Newsorg = ""
String = "Snapchat has 150 million people using the service each day, said people familiar with the matter."
String2 = "The app had 110 million daily users in December, said the people, who asked not to be named because they weren't authorized to speak about the numbers."
split = String.split(", ")

print(split)