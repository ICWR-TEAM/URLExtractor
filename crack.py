import requests
from bs4 import BeautifulSoup

print '''
#############
URL Extractor
#############
* Use http or https!!!
'''
def crack(urlWeb):
	if not urlWeb:
		print "Enter your URL!!!"
		quit()

	header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
	req = requests.get(urlWeb,headers=header).text

	src = BeautifulSoup(req,"html.parser")
	i = 1
	for link in src.findAll("a",href = True):
		i += 1
		print(str(i)+". "+str(link.get("href")))

inputURL = raw_input("Input Your URL: ")
crack(inputURL)
