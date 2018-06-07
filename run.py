from urllib2 import Request,URLError,HTTPError,urlopen

def find():
	f = open("panel.txt","r");
	link = raw_input("Please enter Site url: ")
	print "\n\nChecking links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "We found a live url==",req_link
			print "Happy Hacking :)"

find()
