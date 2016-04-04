import re
import getopt
import sys
import requests
from bs4 import BeautifulSoup
import time
def namu_parse(urls) :

	url = requests.get(urls)
	soup = BeautifulSoup(url.text, "lxml")
	namu = soup.find("textarea", { "class" : "form-control" })

	



def namu_bandal() :

	while 1 :
		url = requests.get("https://namu.wiki/RecentChanges")
		soup = BeautifulSoup(url.text, "lxml")
	
	
		namu1 = soup.find("span", { "class" : "f_r" })
		namu2 = soup.find('href')
		namu1 = namu1.text
		namu1_m = namu1.count('-')
		namu1_m = namu1
		namu1_m = namu1_m.replace('(','')
		namu1_m = namu1_m.replace(')','')
		time.sleep (1)
		print (namu1_m)
		if -1000 > int(namu1_m)  :
			print ("반달!")

		


	



