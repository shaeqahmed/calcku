from flask import Flask, render_template, session, request, redirect, url_for
import json, urllib2
import urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)
x = ''
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
    return render_template('ku.html', hw = x)

url = "http://websites.nylearns.org/rku/2016/6/29/405937/page.aspx"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")
hws = []
table = soup.findAll('table')[1]
# print table
rows = table.find_all('tr')

for row in rows:
     cols = row.find_all('td')
     cols = [ele.text.strip() for ele in cols]
     hws.append([ele for ele in cols if ele]) # Get rid of empty values

for part in hws[1]:
	print part
	#print "\n"
x = part

# ===========================================
# RUN
# ===========================================

if __name__ == '__main__':
    app.debug = True
    app.secret_key = app.config['SECRET_KEY']
    app.run()


