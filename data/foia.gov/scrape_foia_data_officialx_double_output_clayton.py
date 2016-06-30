from urllib2 import urlopen
from urllib import quote
import lxml.html
import requests
import json
import csv
import pprint

from collections import defaultdict


DATA_REPORTS = ["DataRequest","DataExemption","DataAppeal","DataProcessTime","DataFeewaiver","DataPerson","DataBacklog","DataConsultant","RequestDisposition","RequestDenial","RequestPending","Exemption3Statutes","appealDisposition","appealDenialEx","appealDenialOther","appealDenialReason","appealResponseTime","appeal10Pending","processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request","personnelCost","consultation10Oldest","requestCompare","requestBacklog","appealCompare","appealBacklog","feewaiverWaiver","DataPerson"]
DATA_YEARS = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
DATA_AGENCIES = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']

newBaseURL = "https://www.foia.gov/foia/Services/"
newBaseURLAppend = ".jsp?requestYear="

agencyURL = "&agencyName="


def scrape():
	"""
	Scrape all agencies"
	"""
	for dataReport in DATA_REPORTS:
		for year in DATA_YEARS:
			for agency in DATA_AGENCIES:
				scrape_by_args(reports=dataReport, years=year, agencies=agency)


def scrape_by_args(reports=None, years=None, agencies=None):
	"""
	Scrape specific FOIA data by reports, years, agencies
	"""
	if reports is None: reports = DATA_REPORTS
	if type(reports) is not list: reports = [reports]
	if years is None: years = DATA_YEARS
	if type(years) is not list: years = [years]
	if agencies is None: agencies = DATA_AGENCIES
	if type(agencies) is not list: agencies = [agencies]

	for report in reports:
		for year in years:
			for agency in agencies:
				full_url = newBaseURL + report + newBaseURLAppend + year + agencyURL + agency

				#baseURL = newBaseURL + report + newBaseURLAppend + year
				print full_url

				tree = lxml.html.parse(urlopen(quote(full_url, safe="%/:=&?~#+!$,;'@()*[]")))
				table = table_to_list(tree.xpath('//table')[0])

				# Write to table to files
				dataFileName = year + "/" + year + "-" + report + "-" + agency
				jsonFileName = dataFileName + ".json"
				csvFileName = dataFileName + ".csv"

				with open(csvFileName, 'wb') as f:
					writer = csv.writer(f)
					writer.writerows(table)
				with open(jsonFileName, 'wb') as outfile:
					json.dump(table, outfile)


def table_to_list(table):
	dct = table_to_2d_dict(table)
	return list(iter_2d_dict(dct))


def table_to_2d_dict(table):
	result = defaultdict(lambda : defaultdict(unicode))
	for row_i, row in enumerate(table.xpath('./tr')):
		for col_i, col in enumerate(row.xpath('./td|./th')):
			colspan = int(col.get('colspan', 1))
			rowspan = int(col.get('rowspan', 1))
			col_data = col.text_content().strip().replace('\n','')
			while row_i in result and col_i in result[row_i]:
				col_i += 1
			for i in range(row_i, row_i + rowspan):
				for j in range(col_i, col_i + colspan):
					result[i][j] = col_data
	return result


def iter_2d_dict(dct):
	for i, row in sorted(dct.items()):
		cols = []
		for j, col in sorted(row.items()):
			cols.append(col)
		yield cols


def merge():

	# for report in DATA_REPORTS:
	#	with open(report, 'wb') as f
	pass


	"""
	1) For each method, create a CSV file of the same name (i.e. processPending.csv)
	2) Create columns for year and agency
	2) Iterate over CSV files for each year, the method, and agency (i.e. 2008-processingPending-USDA.csv)
	3) For each CSV file, open and read data.
	4) Remove first and last line (assuming they are the headers and the total line)
	5) Add remaining lines to the CSV file opened in step #1. 
	6) Add data for year and agency created in step #2 (i.e. add 2008 and USDA in the columns you created)
	"""


if __name__ == '__main__':
	#scrape()
	scrape_by_args('DataRequest', None, None)
	#merge()
	#print locals()


