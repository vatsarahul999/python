import urllib2
import requests
from bs4 import BeautifulSoup

def getHtmlPage(url):
    response = urllib2.urlopen(url)
    htmlPage = response.read()
    soup = BeautifulSoup(htmlPage)
    return soup


url = raw_input("Enter the url :")
soup = getHtmlPage(url)


print " >>>>>>>>>>>>>>>Form <<<<<<<<<<<<<<<<<<\n"+soup.prettify()

