import time													#import time for delay
import re
from splinter.browser import Browser 						#import Splinter package

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

stickerList = open('msnSticker.txt')						#open the the text file
allStickers = stickerList.readlines()						#read all
resultFile = open('incomeResult.txt', "w")					#report result 

for eachSticker in allStickers:
	print 'Income Statement of %s' % eachSticker,
	print '--------------------------------------------------------------------------------------------------'
	b = Browser('chrome')										#create a browser instance
	loginURL = 'http://investing.money.msn.com/investments/stock-income-statement/?symbol=%s' % eachSticker
	b.visit(loginURL)											#login URL

	year = b.find_by_css("tr.mnrow1")							#find year
	allBold = b.find_by_css("tr.mnboldtopline")					#find all bold lines
	netIncome = b.find_by_css("tr.mnborderbottop3line")			#net income

	yearRaw = year.value										#print year
	yearRaw = re.sub(' ', "\t\t", yearRaw)
	print "Year:\t\t\t%s" % yearRaw

	totalRevRaw = allBold[0].value								#print total revenue
	totalRevArray = totalRevRaw.split("\n")
	totalRevArray[1] = re.sub(' ', "\t", totalRevArray[1])
	print "Total Revenue:\t\t%s" % totalRevArray[1]

	grossProfitRaw = allBold[1].value							#print gross profit
	grossProfitArray = grossProfitRaw.split("\n")
	grossProfitArray[1] = re.sub(' ', "\t", grossProfitArray[1])
	print "Gross Profit:\t\t%s" % grossProfitArray[1]

	listOfRev = totalRevArray[1].split("\t")					#calcuating profit margin
	listOfGross = grossProfitArray[1].split("\t")
	margin = ""	
	count = 0	
	marginSum = 0											
	for i in range(len(listOfRev)):
		listOfRev[i] = re.sub(",", "", listOfRev[i])
		tempRev = float(listOfRev[i])
		listOfGross[i] = re.sub(",", "", listOfGross[i])
		tempGross = float(listOfGross[i])
		tempMargin = tempGross / tempRev * 100
		marginSum += tempMargin
		margin += "%.2f" % tempMargin
		margin += "%\t\t"
		count += 1
	avgMargin = marginSum / count
	print bcolors.HEADER
	print "Profit Margin:\t\t%s" % margin,
	print bcolors.OKGREEN

	netRaw = netIncome.value									#print net income
	netArray = netRaw.split("\n")
	netArray[1] = re.sub(' ', "\t", netArray[1])
	print "Net Income:\t\t%s" % netArray[1]

	listOfNet = netArray[1].split("\t")							#calculate % of net
	listOfRev = totalRevArray[1].split("\t")					#calcuating profit margin
	netPer = ""
	count = 0
	netSum = 0
	for i in range(len(listOfNet)):
		listOfNet[i] = re.sub(",", "", listOfNet[i])
		listOfRev[i] = re.sub(",", "", listOfRev[i])
		tempNet = float(listOfNet[i])
		tmpRevPer = float(listOfRev[i])
		tempNetPer = tempNet / tmpRevPer * 100
		netSum += tempNetPer
		count += 1
		netPer += "%.2f" % tempNetPer
		netPer += "%\t\t"
	avgNet = netSum / count
	
	eachSticker = re.sub("\n", "", eachSticker)
	result = '%s %.2f %.2f\n' % (eachSticker, avgMargin, avgNet)

	print bcolors.HEADER 
	print "Net Percentage:\t\t%s" % netPer,
	print bcolors.OKGREEN
	print '--------------------------------------------------------------------------------------------------\n'
	b.quit()
	resultFile.write(result)
resultFile.close()

