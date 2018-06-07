from urllib2 import Request
import URLError
import HTTPError
import urlopen
def find():
	file = open("panel.txt","r");
	site = raw_input("Please enter Site url: ")
	print "\n\nChecking links : \n"
	while True:
		s = file.readline()
		if not s:
			break
		target = site.replace("http://","")#add http to the front of the website
		final = target+site+"/"+s #combine http,input site and panel 
		test = Request(final)
		try:
			response = urlopen(test)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "We found a live url==",final
			print "Happy Hacking :)"

find()
