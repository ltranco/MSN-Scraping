import time													#import time for delay
import re
import MySQLdb
from splinter.browser import Browser 						#import Splinter package

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#stickerList = open('msnSticker.txt')						#open the the text file
#allStickers = stickerList.readlines()						#read all
#resultFile = open('incomeResult.txt', "w")					#report result 

eachSticker = 'T'

print 'Income Statement of %s' % eachSticker
b = Browser('chrome')										#create a browser instance
loginURL = 'http://investing.money.msn.com/investments/stock-income-statement/?symbol=%s' % eachSticker
b.visit(loginURL)											#login URL

all_year = b.find_by_css("tr.mnrow1").find_by_tag("td")
year = ''
for each_year in all_year:
	if each_year.value != "":
		year += '%s\t' % each_year.value 
print year

mnfh = b.find_by_css("tr.mnfh")
mnfh_bold = b.find_by_css("tr.mnboldtopline")
mnfh_three = b.find_by_css("tr.mnborderbottop3line")

want = [6, 7, 8, 10, 11, 12, 14, 15, 17, 21]
for i in range(len(mnfh)):
	if not i in want:
		continue
	mnfh_row = mnfh[i].find_by_tag("td")
	data = ''
	for mnfh_col in mnfh_row:
		if mnfh_col.value != "" and mnfh_col.value != "\n":
			data += '%s\t' % mnfh_col.value
	print data

for i in range(len(mnfh_bold)):
	mnfh_row = mnfh_bold[i].find_by_tag("td")
	data = ''
	for mnfh_col in mnfh_row:
		if mnfh_col.value != "" and mnfh_col.value != "\n":
			data += '%s\t' % mnfh_col.value
	print data

for i in range(len(mnfh_three)):
	mnfh_row = mnfh_three[i].find_by_tag("td")
	data = ''
	for mnfh_col in mnfh_row:
		if mnfh_col.value != "" and mnfh_col.value != "\n":
			data += '%s\t' % mnfh_col.value
	print data
b.quit()


