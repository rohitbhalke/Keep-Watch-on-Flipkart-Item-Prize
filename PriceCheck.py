import urllib2, bs4
import webbrowser  #for playing song
import time


# enter url of that product which you want to track
url = "http://www.flipkart.com/forevercarat-adorable-silver-diamond-sterling-plated-ring/p/itmdyz3eq6zugnky?pid=RNGDYZ3EHNJQMTXQ&otracker=from-search&srno=t_6&query=rings&ref=ded8f951-c8d9-4970-904f-342d6cb63090"
req = urllib2.urlopen(url)
raw = req.read()
soup = bs4.BeautifulSoup(raw)

myprice= 15000 #enter the price in which you are interested

def fetchDataAndCheckPrice(url):
	objectItem = soup.find_all("span", class_="selling-price omniture-field")


	for ob in objectItem:
		price = ''.join(ob.findAll(text=True))

	price = price[4:].replace(",","") 	
	print price

	return price

while 1:
	price = fetchDataAndCheckPrice(url);
	if (int(price)<myprice):
		print "Yes"
		webbrowser.open("https://www.youtube.com/watch?v=hfgu9UgRhsc")
		break;
	else:
		print "No"	
		time.sleep(300)		#if price is not low run this code again after 300 seconds


