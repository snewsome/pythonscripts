import gspread
import sys
import os
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials

#x = raw_input('Give a row value ')
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('shawns_test.json', scope)
client = gspread.authorize(creds)

gc = gspread.authorize(creds)

sheet = gc.open("ShawnTest").sheet1

if sheet.cell(1,1).value=="done":
	sheet.update_cell(1, 2, 'Kevi is stupid!')
	print("Successful")
	
else :
	print("Unsuccessful")
