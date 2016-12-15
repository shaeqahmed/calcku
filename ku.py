from flask import Flask, render_template, session, request, redirect, url_for
import json, urllib2
import urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)

# ===========================================
# ROUTES
# ===========================================
@app.route('/')
@app.route('/home/')
def home():
    if 'user' in session:
        u = session['user']
    else:
        u = ""
    return render_template('ku.html', hws = formattedhws)

url = "http://websites.nylearns.org/rku/2016/6/29/405937/page.aspx"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")
hws = []
table = soup.findAll('table')[1]
# print table
rows = table.find_all('tr')

for row in rows:
     cols = row.find_all('td')
     cole =[]
     if len(cols) >= 4:
     	cole.append(cols[0].text.strip())
     	cole.append(cols[1].text.strip())
     	if cols[2].find('a'):
     		intt = cols[2].text.strip().index(cols[2].find('a').text.strip())
     		cole.append(cols[2].text.strip()[0:intt]+str(cols[2].find('a')))
     	else:
     		cole.append(cols[2].text.strip())
     	cole.append(cols[3].text.strip())
     #if len(cole) != 0:
    	hws.append(cole) # Get rid of empty values

hwss = [s for s in hws if len(s) == 4]
hwss = hwss[1:]



#print hwss
formattedhws = []

for i in range(len(hwss)):
	date = hwss[i][0]
	aim = hwss[i][1]
	#aim = aim.encode('ascii', 'ignore').decode('ascii')
	#print hws[1][2]
	hwnum =""
	hw = hwss[i][2]
	if i != 26:
		hwnum = hwss[i][2][0: hwss[i][2].find(' ')]
		hw = hwss[i][2][hwss[i][2].find(' '):]
	due = hwss[i][3]
	formattedhws.append([hwnum, due, aim, hw, date])

# for a in formattedhws:
# 	for x in a:
# 		print x+"\n"
# 	print "\n--------------------------------------------------------"


# ===========================================
# RUN
# ===========================================

if __name__ == '__main__':
    app.debug = True
    app.secret_key = app.config['SECRET_KEY']
    app.run()


