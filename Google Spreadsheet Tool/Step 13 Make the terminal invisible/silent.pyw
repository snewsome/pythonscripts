

import time
import urllib2
import json
import gspread
import sys
import os
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials
from apscheduler.schedulers.blocking import BlockingScheduler



def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def some_job():
    if sheet.cell(1,1).value=="continue":
		# Automatically geolocate the connecting IP
		f = urllib2.urlopen('http://freegeoip.net/json/')
		json_string = f.read()
		f.close()
		location = json.loads(json_string)
		#print(location)
		location_city = location['city']
		location_state = location['region_name']
		location_country = location['country_name']
		location_zip = location['zip_code']
		sheet.update_cell(1, 2, location)

scheduler = BlockingScheduler()
while True:
	time.sleep(1800)
	while internet_on():
		#scheduler.add_job(some_job, 'interval', seconds=10)
		#scheduler.start()
		# use creds to create a client to interact with the Google Drive API
		scope = ['https://spreadsheets.google.com/feeds']
		creds = ServiceAccountCredentials.from_json_keyfile_name('shawns_test.json', scope)
		client = gspread.authorize(creds)

		gc = gspread.authorize(creds)

		sheet = gc.open("ShawnTest").sheet1
		some_job()
		time.sleep(10)