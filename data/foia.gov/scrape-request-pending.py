from urllib2 import urlopen
import lxml.html
import requests
import json
import csv

# dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
# dataAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']
# dataAgencies = ['DoD','ED']
dataReport = "RequestPending"
dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
dataAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']
# dataAgencies = ['DoD','ED']


# https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2008&agencyName=DoD

baseURL = "https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear="
# 2014
agencyURL = "&agencyName="
# FDIC"

for year in dataYears:
	# print baseURL + year
	for agency in dataAgencies:
		# print baseURL + year + agencyURL + agency
		tree = lxml.html.parse(urlopen(baseURL + year + agencyURL + agency))
		# table = [[th.text_content().strip() for th in tree.xpath('//th') if th.text_content().strip()]]
		# print table
		thead = ["Component", "Number Pending - Simple","Median No. of Days - Simple","Average No. of Days - Simple","Number Pending - Complex","Median No. of Days - Complex","Average No. of Days - Complex","Number Pending - Expedited","Median No. of Days - Expedited","Average No. of Days - Expedited","Year","Agency"]
		table = []
		table.append(thead)
		# print table
		#tableHead = ([th.text_content() for th in tree.xpath('//th')])
		for tr in tree.xpath('//tr'):
			row = []
			for td in tr.xpath('//td'):
				content = td.text_content().strip()
				if content not in ["", "\\u00a0"]:
					# content = content + year
					row.append(content)
					# print row
					# row.append(year)
			row.append(year)
			row.append(agency)
			print row
			table.append(row)
		# print table

		#tableBody = ([td.text_content() for td in tree.xpath('//td')])
		#tableData = tableHead + tableBody
		# print tableData
		# jsonFileName = year + "/" + year + "-" + agency + ".json"
		# make csv with json. what could go wrong?
		"""dataFileName = "created/" + year + "-" + dataReport + "-" + agency
		jsonFileName = dataFileName + ".json"
		csvFileName = dataFileName + ".csv"

		with open(csvFileName, 'w') as outfile:
			json.dump(table, outfile)
		with open(csvFileName, 'w') as f:
			writer = csv.writer(f)
			writer.writerows(table)"""
		# with open(jsonFileName, 'w') as outfile:
		#	json.dump(table, outfile)