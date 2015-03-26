import urllib2, bs4
import webbrowser  #for playing song
import time


# enter url of that product which you want to track
url = "http://www.flipkart.com/rosemary-rm-0038-hand-held-bag/p/itme2fk9x8nd46rs?pid=HMBE2FK9XBANJWYC&srno=b_2&ref=000fa332-69d8-4047-a350-cb1bc15882d9"
req = urllib2.urlopen(url)
raw = req.read()
soup = bs4.BeautifulSoup(raw)

myprice= 15000 #enter the price in which you are interested

def fetchDataAndCheckPrice(url):

	objectItem = soup.find_all("span", class_="selling-price omniture-field")

	if objectItem:
		for ob in objectItem:
			price = ''.join(ob.findAll(text=True))

		price = price[4:].replace(",","") 	
		print price

		return price
	else:
		return -1
		
while 1:
	price = fetchDataAndCheckPrice(url);
	if(int(price)==-1):
		
		print "Sorry your wish is out of stock :("  #if item is out of stock
		break	
	elif(int(price)<myprice):
		print "Yes"
		webbrowser.open("https://www.youtube.com/watch?v=hfgu9UgRhsc")
		break;
	else:
		print "No"	
		time.sleep(100)		#if price is not low run this code again after 5 seconds
	

	
	

