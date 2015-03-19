import urllib2, bs4
import webbrowser  #for playing song
import time

url = "http://www.flipkart.com/forevercarat-adorable-silver-diamond-sterling-plated-ring/p/itmdyz3eq6zugnky?pid=RNGDYZ3EHNJQMTXQ&otracker=from-search&srno=t_6&query=rings&ref=ded8f951-c8d9-4970-904f-342d6cb63090"
req = urllib2.urlopen(url)
raw = req.read()
soup = bs4.BeautifulSoup(raw)

def fetchDataAndCheckPrice(url):
	objectCamera = soup.find_all("span", class_="selling-price omniture-field")

# extract the prize from span conatining prize in html page 
	for ob in objectCamera:
		price = ''.join(ob.findAll(text=True))

	price = price[4:].replace(",","") 	
	print price

	return price

while 1:
	price = fetchDataAndCheckPrice(url);
	if (int(price)<15000):
		print "Yes"
		webbrowser.open("https://www.youtube.com/watch?v=hfgu9UgRhsc")
		break;
	else:
		print "No"	
		time.sleep(100)		#if price is not low run this code again after 5 seconds




#print objectCamera
# print soup.get_text()
