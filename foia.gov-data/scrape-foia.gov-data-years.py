import lxml.html as LH
import requests
import json

dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
dataAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']

baseURL = "http://www.foia.gov/foia/Services/processingSimple.jsp?requestYear="
# 2014
agencyURL = "&agencyName="
# FDIC"

for year in dataYears:
	print baseURL + year
	for agency in dataAgencies:
		print baseURL + year + agencyURL + agency
# test = baseURL + dataYears[0]
# print test

# treeURL = baseURL + yearURLVar + agencyURL + agencyURLVar

# x = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
# for i in x:
#	print i

tree = LH.parse("http://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2014&agencyName=FDIC")

# print([th.text_content() for th in tree.xpath('//th')])
# print([td.text_content() for td in tree.xpath('//td')])

tableHead = ([th.text_content() for th in tree.xpath('//th')])
tableBody = ([td.text_content() for td in tree.xpath('//td')])
tableData = tableHead + tableBody
# print tableData

# with open('2014-FDIC.json', 'w') as outfile:
#	json.dump(tableData, outfile)