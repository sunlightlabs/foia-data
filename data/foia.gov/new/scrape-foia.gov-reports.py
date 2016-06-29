from urllib2 import urlopen
# import lxml.html as LH
import lxml.html
import requests
import json


dataReports = ["DataRequest","DataExemption","DataAppeal","DataProcessTime","DataFeewaiver","DataPerson","DataBacklog","DataConsultant","RequestDisposition","RequestDenial","RequestPending","Exemption3Statutes","appealDisposition","appealDenialEx","appealDenialOther","appealDenialReason","appealResponseTime","appeal10Pending","processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request","personnelCost","consultation10Oldest","requestCompare","requestBacklog","appealCompare","appealBacklog","feewaiverWaiver","DataPerson"]
dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
dataAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']
# dataAgencies = ['DoD','ED']



# baseURL = "https://www.foia.gov/foia/Services/processing10Request.jsp?requestYear="
newBaseURL = "https://www.foia.gov/foia/Services/"
newBaseURLAppend = ".jsp?requestYear="
# baseURL = newBaseURL + dataReport + newBaseURLAppend
# 2014
agencyURL = "&agencyName="
# FDIC"
for dataReport in dataReports:
	baseURL = newBaseURL + dataReport + newBaseURLAppend
	for year in dataYears:
		# print baseURL + year
		for agency in dataAgencies:
			# print baseURL + year + agencyURL + agency
			# https://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2015&agencyName=USDA
			# tree = LH.parse(baseURL + year + agencyURL + agency)
			# print baseURL + year + agencyURL + agency
			tree = lxml.html.parse(urlopen(baseURL + year + agencyURL + agency))
			tableHead = ([th.text_content() for th in tree.xpath('//th')])
			tableBody = ([td.text_content() for td in tree.xpath('//td')])
			tableData = tableHead + tableBody
			# print tableData
			jsonFileName = year + "/" + year + "-" + dataReport + "-" + agency + ".json"
			# print jsonFileName
			with open(jsonFileName, 'w') as outfile:
				json.dump(tableData, outfile)