import re
import getopt
import sys
import requests
from bs4 import BeautifulSoup
import time
def namu_parse() :

	url = requests.get("https://namu.wiki/edit/%EC%88%98%EC%95%84%EB%B2%A0")
	soup = BeautifulSoup(url.text, "lxml")


	namu = soup.find("textarea", { "class" : "form-control" })

	namu_text = namu.text
	namu_cnt = namu_text.count(']')
	namu_cnt2 = namu_text.find("[*")
	namu_cnt2 = namu_text.find('[*(*)')
	namu_text = namu_text.replace("[*","각주")
	namu_text = namu_text.replace("<<","[")
	namu_text = namu_text.replace(">>","]")
	namu_text = namu_text.replace("[[","훌라")
	namu_text = namu_text.replace("]]","라훌")

	namu_text = namu_text.replace("[","[[")

	namu_text = namu_text.replace("]","]]")
	namu_text = namu_text.replace("\"]]","]]")
	namu_text = namu_text.replace("[[wiki:\"","[[")

	namu_text = namu_text.replace("훌라목차라훌","[목차]")
	namu_text = namu_text.replace("훌라각주라훌","[각주]")
	namu_text = namu_text.replace("훌라","[[")
	namu_text = namu_text.replace("라훌","]]")
	namu_text = namu_text.replace("각주","[*")
	
	print (namu_cnt2)
	print (namu_text[namu_cnt2+2:namu_cnt2+100])




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

		


	



