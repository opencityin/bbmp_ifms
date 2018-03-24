# coding=utf-8
import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
import datetime
import json
from datetime import datetime
#from bs4 import BeautifulSoup


def step2_insert_json_payments_data():
	with open('payments.json', 'r') as outfile:
		data = json.load(outfile)

	db = dataset.connect('sqlite:////home/thej/code/bbmp_ifms/ifms.sqlite')
	db.begin()
	vssWB = db['payments']

	for data_item in data:
		#print str(data_item)
		r_id = data_item["id"]
		print str(r_id)
		wodetails = data_item["wodetails"]
		#print str(wodetails)
		soup = BeautifulSoup(wodetails)
		billstatus_jobnumber = soup.a.text
		jobnumber_splits = billstatus_jobnumber.split("-")
		billstatus_ward = jobnumber_splits[0]
		if billstatus_ward == "R":
			billstatus_ward = jobnumber_splits[1]
		data_item["jobnumber"] =billstatus_jobnumber
		data_item["ward"]= billstatus_ward
		print str(data_item)
		if vssWB.find_one(id=r_id):
			print "exists"
		else:
			vssWB.insert(data_item)
			db.commit()



def step1_pull_payments():
	pagenum = 0
	url = "http://218.248.45.166:8092/vssWB/vss00CvStatusData.php?pAction=LoadPaymentGridData&"
	url = url + "pDateFrom=30-Sep-2017&pDateTo=30-Mar-2018&"
	url = url +"pBudgetHeadID=-1&filterscount=0&groupscount=0&sortorder=&pagesize=5&recordstartindex=0&recordendindex=5&_=1502250689374"
	url = url +"pagenum="+str(pagenum)+"&"
	url = url + """pWardIDs=300,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315&pDDOID=-1&pDDOIDs=15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,563,564,566,567,568,569,570,571,572,573,574,575,576,577,578,581,583,584,585,586,587,588,590,591,592,593,594,595,597,598,599,600,601,602,603,604,605,606,607,608,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,760,580"""

	# pagenum variable is not used
	print str(url)
	r = requests.get(url)
	print "Got request"
	if r.status_code == 200:
		print "OK"
		data = r.json()
		with open('payments.json', 'w') as outfile:
			json.dump(data, outfile)



def step3_workorder_update():
	db = dataset.connect('sqlite:////home/thej/code/bbmp_ifms/ifms.sqlite')
	db.begin()

	vssWB = db['payments']

	for db_row in vssWB:
		wodetails = db_row["wodetails"]
		soup = BeautifulSoup(wodetails)
		billstatus_jobnumber = soup.a.text
		jobnumber_splits = billstatus_jobnumber.split("-")
		billstatus_ward = jobnumber_splits[0]
		if billstatus_ward == "R":
			billstatus_ward = jobnumber_splits[1]
		update_db_row = {}
		update_db_row["billstatus_jobnumber"] =billstatus_jobnumber
		update_db_row["billstatus_ward"]= billstatus_ward
		update_db_row["id"] = db_row["id"]
		vssWB.update(update_db_row, ['id'])
	db.commit()

def step4_pull_billid():
	db = dataset.connect('sqlite:////home/thej/code/bbmp_ifms/ifms.sqlite')
	db.begin()
	payments = db['payments']
	bills = db['bills']
	for db_row in payments:
		if db_row["bills_added"] == 1:
			print "SKIPPING"
			continue
		jobnumber = db_row["jobnumber"]
		url = "http://218.248.45.166:8092/vssWB/vss00CvStatusData.php?pAction=LoadTypeCombo&pJobNumber="+jobnumber+"&pSelection=1&filterscount=0&groupscount=0&pagenum=0&pagesize=10&recordstartindex=0&recordendindex=17.8&_=1503727209861"
		# [{"wbid":"56","job":"175-12-000032<br\/>Engaging tractor and labour in Bommanahalli ward for the year 2012.","wodetails":"WO-000084\/02-Jun-2012<br\/>SBR-000012\/30-May-2013<br\/>BR-000067\/31-May-2013<br\/>CBR-000001\/01-Jun-2015"}]
		r = requests.get(url)
		if r.status_code == 200:

			data = r.json()
			print str(data)
			for data_row in data:
				update_data = {}
				update_data["payment_id"] = db_row["id"]
				update_data["jobnumber"] = db_row["jobnumber"]
				update_data["ward"] = db_row["ward"]

	 			update_data["wodetails"] = data_row["wodetails"]
	 			update_data["wbid"] = data_row["wbid"]
	 			update_data["job"] = data_row["job"]
	 			bills.insert(update_data)
	 	payments.update(dict({"bills_added": 1, "id":db_row["id"] }), ["id"])
		db.commit()

def step5_split_update_bill_details():
	db = dataset.connect('sqlite:////home/thej/code/bbmp_ifms/ifms.sqlite')
	db.begin()
	bills = db['bills']
	for db_row in bills:
		if db_row["bills_split_added"] == 1:
			print "SKIPPING"
			continue
		wodetails = db_row["wodetails"]
		#WO-000388/01-Mar-2013<br/>SBR-000186/30-Mar-2013<br/>BR-000010/30-Apr-2013<br/>CBR-000034/06-Jun-2015
		split_bills = wodetails.split("<br/>")
		for bill_detail in split_bills:
			bill_detail = bill_detail.encode('utf-8')
			print str(bill_detail)
			if bill_detail.startswith("WO-"):
				bill = bill_detail.split("/")			
				db_row["wo_id"] = bill[0]
				if len(bill) > 1 and len(bill[1]) > 10:
					db_row["wo_date"] = datetime_object = datetime.strptime(bill[1], '%d-%b-%Y')
			elif bill_detail.startswith("SBR-"):
				bill = bill_detail.split("/")
				db_row["sbr_id"] = bill[0]
				if len(bill) > 1 and len(bill[1]) > 10:
					db_row["sbr_date"] = datetime_object = datetime.strptime(bill[1], '%d-%b-%Y')
			elif bill_detail.startswith("BR-"):
				bill = bill_detail.split("/")
				db_row["br_id"] = bill[0]
				if len(bill) > 1 and len(bill[1]) > 10:
					db_row["br_date"] = datetime_object = datetime.strptime(bill[1], '%d-%b-%Y')				
			elif bill_detail.startswith("CBR-"):
				bill = bill_detail.split("/")
				db_row["cbr_id"] = bill[0]
				if len(bill) > 1 and len(bill[1]) > 10:
					db_row["cbr_date"] = datetime_object = datetime.strptime(bill[1], '%d-%b-%Y')


		print str(db_row)
		db_row["bills_split_added"] = 1
	 	bills.update(db_row, ["id"])
		db.commit()

def main():
	#step1_pull_payments()
	#step2_insert_json_payments_data()
	#step3_workorder_update()
	#step4_pull_billid()
	step5_split_update_bill_details()

if __name__ == "__main__":
	main()

