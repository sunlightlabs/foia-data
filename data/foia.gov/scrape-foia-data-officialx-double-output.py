from urllib2 import urlopen
import lxml.html
import requests
import json
import csv


# dataReports = ["DataRequest","DataExemption","DataAppeal","DataProcessTime","DataFeewaiver","DataPerson","DataBacklog","DataConsultant","RequestDisposition","RequestDenial","RequestPending","Exemption3Statutes","appealDisposition","appealDenialEx","appealDenialOther","appealDenialReason","appealResponseTime","appeal10Pending","processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request","personnelCost","consultation10Oldest","requestCompare","requestBacklog","appealCompare","appealBacklog","feewaiverWaiver","DataPerson"]
# dataReports = ["processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request"]
# dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
# dataAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']
dataReports = ["processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request"]
dataYears = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
dataAgencies = ['USDA']




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
			# tree = LH.parse(baseURL + year + agencyURL + agency)
			tree = lxml.html.parse(urlopen(baseURL + year + agencyURL + agency))
			table = [[th.text_content().strip() for th in tree.xpath('//th') if th.text_content().strip()]]
			#tableHead = ([th.text_content() for th in tree.xpath('//th')])
			for tr in tree.xpath('//tr'):
				row = []
				for td in tr.xpath('//td'):
					content = td.text_content().strip()
					if content not in ["", "\\u00a0"]:
						row.append(content)
					table.append(row)
					#tableBody = ([td.text_content() for td in tree.xpath('//td')])
					#tableData = tableHead + tableBody
					# print tableData
					# jsonFileName = year + "/" + year + "-" + agency + ".json"
					# make csv with json. what could go wrong?
				# jsonFileName = year + "/" + year + "-" + dataReport + "-" + agency + ".csv"
				# with open(jsonFileName, 'w') as outfile:
				#	json.dump(table, outfile)
				# with open(jsonFileName, 'w') as f:
				#	writer = csv.writer(f)
				#	writer.writerows(table)
				dataFileName = year + "/" + year + "-" + dataReport + "-" + agency
				jsonFileName = dataFileName + ".json"
				csvFileName = dataFileName + ".csv"

				with open(csvFileName, 'w') as outfile:
					json.dump(table, outfile)
				with open(csvFileName, 'w') as f:
					writer = csv.writer(f)
					writer.writerows(table)
				with open(jsonFileName, 'w') as outfile:
					json.dump(table, outfile)


def scrape():
	pass
	# TODO move code here



def merge():
	pass
	"""
	Problem to fix first
	1) Fix number of headers in CSV files not matching row data.
	2) Figure out why number of rows doesn’t match number of rows found in HTML table element (i.e. USDA 2008 processPending)

	Merge algorithm psuedocode
	1) For each method, create a CSV file of the same name (i.e. processPending.csv)
	2) Create columns for year and agency
	2) Iterate over CSV files for each year, the method, and agency (i.e. 2008-processingPending-USDA.csv)
	3) For each CSV file, open and read data.
	4) Remove first and last line (assuming they are the headers and the total line)
	5) Add remaining lines to the CSV file opened in step #1. 
	6) Add data for year and agency created in step #2 (i.e. add 2008 and USDA in the columns you created)
	"""


if __name__ == '__main__':
	scrape()
	merge()



