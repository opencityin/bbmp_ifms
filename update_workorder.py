# coding=utf-8
import sys
import sqlite3 as lite
import requests
import time
from bs4 import BeautifulSoup
import dataset
import time
import datetime
import json


db = dataset.connect('sqlite:////home/thej/code/bbmp_ifms/ifms.sqlite')
db.begin()

vssWB = db['payments']

for db_row in vssWB:
	wodetails = db_row["wodetails"]
	soup = BeautifulSoup(wodetails, 'html.parser')
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

	# billstatus_job = 
	# billstatus_wbid = wodetails["wbid"]
	# billstatus_wodetails = 

# http://218.248.45.166:8092/vssWB/vss00CvStatusData.php?pAction=LoadTypeCombo&pJobNumber=175-12-000032&pSelection=1&filterscount=0&groupscount=0&pagenum=0&pagesize=10&recordstartindex=0&recordendindex=17.8&_=1503727209861
# [{"wbid":"56","job":"175-12-000032<br\/>Engaging tractor and labour in Bommanahalli ward for the year 2012.","wodetails":"WO-000084\/02-Jun-2012<br\/>SBR-000012\/30-May-2013<br\/>BR-000067\/31-May-2013<br\/>CBR-000001\/01-Jun-2015"}]



#http://218.248.45.166:8092/vssWB/vss00CvStatusData.php?pAction=LoadDetails&pWorkBillID=56


# work_bill_billtype =work_bill["billtype"]
# budget =work_bill["budget"]
# cbrdate =work_bill["cbrdate"]
# cbrnumber =work_bill["cbrnumber"]
# contractoremail =work_bill["contractoremail"]
# contractormobile1 =work_bill["contractormobile1"]
# contractorname =work_bill["contractorname"]
# currentlevel =work_bill["currentlevel"]
# currentlevelname =work_bill["currentlevelname"]
# dbrdate =work_bill["dbrdate"]
# dbrnumber =work_bill["dbrnumber"]
# ddoname =work_bill["ddoname"]
# deduction =work_bill["deduction"]
# deductioninwords =work_bill["deductioninwords"]
# gross =work_bill["gross"]
# grossinwords =work_bill["grossinwords"]
# nett =work_bill["nett"]
# nettinwords =work_bill["nettinwords"]
# rtgs =work_bill["rtgs"]
# rtgsdate =work_bill["rtgsdate"]
# sbrdate =work_bill["sbrdate"]
# sbrnumber =work_bill["sbrnumber"]
# tvccrequiredyn =work_bill["tvccrequiredyn"]
# wcdescription =work_bill["wcdescription"]

# r = requests.get(url)
# print "Got request"
# if r.status_code == 200:
# 	print "OK"
# 	data = r.json()
# 	for data_item in data:
# 		print str(data_item)
# 		id = data_item["id"]
# 		# alt_id = id
# 		# del data_item["id"]
# 		# data_item["alt_id"]=alt_id
# 		# data_item["pagenum"]=pagenum
# 		vssWB.insert(data_item)

# 	pagenum = pagenum + 1
# 	print "pagenum="+str(pagenum)
# 	db.commit()
# else:
# 	print "Error "

