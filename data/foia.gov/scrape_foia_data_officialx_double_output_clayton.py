from urllib2 import urlopen, HTTPError
from urllib import quote
import lxml.html
import requests
import json
import csv
import pprint
import time
import os
import pandas as pd
import traceback

from collections import defaultdict

DATA_DIR = 'data'
DATA_REPORTS = ["DataRequest","DataExemption","DataAppeal","DataProcessTime","DataFeewaiver","DataPerson","DataBacklog","DataConsultant","RequestDisposition","RequestDenial","RequestPending","Exemption3Statutes","appealDisposition","appealDenialEx","appealDenialOther","appealDenialReason","appealResponseTime","appeal10Pending","processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request","personnelCost","consultation10Oldest","requestCompare","requestBacklog","appealCompare","appealBacklog","feewaiverWaiver","DataPerson"]
DATA_YEARS = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
DATA_AGENCIES = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']

newBaseURL = "https://www.foia.gov/foia/Services/"
newBaseURLAppend = ".jsp?requestYear="

agencyURL = "&agencyName="

try:
	CACHE = json.load(open('cache_manifest.json', 'rb'))
except:
	CACHE = {}

def scrape(cached=True):
	"""
	Scrape all agencies"
	"""
	for dataReport in DATA_REPORTS:
		for year in DATA_YEARS:
			for agency in DATA_AGENCIES:
				scrape_by_args(reports=dataReport, years=year, agencies=agency, cached=cached)


def scrape_by_args(reports=None, years=None, agencies=None, cached=True):
	"""
	Scrape specific FOIA data by reports, years, agencies
	"""
	if reports is None: reports = DATA_REPORTS
	if type(reports) is not list: reports = [reports]
	if years is None: years = DATA_YEARS
	if type(years) is not list: years = [years]
	if agencies is None: agencies = DATA_AGENCIES
	if type(agencies) is not list: agencies = [agencies]

	def download(full_url, retry=3):
		for i in range(0, retry):
			try:
				if not cached or full_url not in CACHE.keys():
					return lxml.html.parse(urlopen(quote(full_url, safe="%/:=&?~#+!$,;'@()*[]")))
				else:
					print full_url + ' already downloaded according to cache.'
					return
			except HTTPError:
				if i < retry:
					print 'Failed to download from ' + full_url + '. Retrying in 5 seconds.'
					time.sleep(5)
				else:
					raise

	for report in reports:
		for year in years:
			for agency in agencies:
				full_url = newBaseURL + report + newBaseURLAppend + year + agencyURL + agency

				print full_url
				tree = download(full_url)
				if tree is None:
					continue

				table = table_to_list(tree.xpath('//table')[0])

				# Write to table to files
				dataFileName = DATA_DIR + "/" + year + "-" + report + "-" + agency
				jsonFileName = dataFileName + ".json"
				csvFileName = dataFileName + ".csv"

				with open(csvFileName, 'wb') as f:
					writer = csv.writer(f)
					writer.writerows(table)
				with open(jsonFileName, 'wb') as outfile:
					json.dump(table, outfile)

				# assume successful download
				CACHE[full_url] = csvFileName


def table_to_list(table):
	dct = table_to_2d_dict(table)
	return list(iter_2d_dict(dct))


def table_to_2d_dict(table):
	result = defaultdict(lambda : defaultdict(unicode))
	for row_i, row in enumerate(table.xpath('./tr')):
		for col_i, col in enumerate(row.xpath('./td|./th')):
			colspan = int(col.get('colspan', 1))
			rowspan = int(col.get('rowspan', 1))
			col_data = col.text_content().strip().replace('\n','').encode('utf-8')
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
		if cols[-1] == '':  # if last column is blank, drop it
			del cols[-1]
		yield cols


def merge(agencies=None):

	filelist = os.listdir(DATA_DIR)
	if type(agencies) is None: agencies = DATA_REPORTS
	if type(agencies) is not list: agencies = [agencies]

	def merge_method(method):
		files = [filename for filename in filelist if method in filename and 'csv' in filename and "full" not in filename]
		if len(files) == 0:
			return pd.DataFrame([])
		else:
			df = pd.concat((edit(f) for f in files))
			if 'Component' in df.columns:
				df = df[df.Component.str.contains('Total') == False] # remove rows containing Total in the Component column
				if df['Component'].iloc[0] == '': # handle subheaders
					subheaders = df.iloc[1].copy() # get the first row under header because it's defintely a subheader if the Component is a blank string
					subheaders[0:2] = '' # clear agency data
					df = df[df.Component != ''] # remove rows where component is an empty string
					df.iloc[0] = subheaders # set subheader
			return df

	def edit(filename):  # Takes filename, returns dataframe which can be aggregated.
		try:
			parts = os.path.splitext(filename)[0].split('-')
			year = parts[0]
			agency = '-'.join(parts[2:])
			tempdf = pd.read_csv(os.path.join(DATA_DIR, filename), na_values=[], na_filter=False)
			
			tempdf.insert(0, 'Year', pd.Series([year for i in range(0, len(tempdf.index))]))  # Add year column
			tempdf.insert(1, 'Agency', pd.Series([agency for i in range(0, len(tempdf.index))]))  # Add year column
			tempdf = tempdf.dropna(axis=1, how='all') # remove columns with empty fields

			return tempdf
		except:
			print filename + ' failed.'
			print traceback.format_exc()
			return
	
	for method in agencies:
		print "Attempting to merging " + method
		tempcsv = merge_method(method)
		if type(tempcsv) is str == True:
			print("None found of " + method)
		else:
			tempcsv.to_csv(method + "_full.csv", index=False)
			print 'No errors encountered while merging ' + method


if __name__ == '__main__':
	#scrape_by_args('processingPending', None, None, False)
	#scrape_by_args('RequestDisposition', None, None, False)
	"""
	try:
		scrape(cached=True)
		#scrape_by_args('Exemption3Statutes', '2008', 'DOC', False)
	except:
		print traceback.format_exc()
		print 'Critical error in scrape, dumping downloaded links to cache.'
	finally:
		json.dump(CACHE, open('cache_manifest.json', 'wb'), indent=2)
	"""
	merge('processingPending')
	#print locals()


