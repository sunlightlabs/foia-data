from urllib2 import urlopen
import lxml.html
import requests
import json
import csv


tree = lxml.html.parse(urlopen('https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2015&agencyName=DoD'))
table = [[th.text_content().strip() for th in tree.xpath('//th') if th.text_content().strip()]]
row = []
year = "2015"
agencyName = "DoD"

for tr in tree.xpath('//form/table/tr'):
	#row = []

	for td in tr.xpath('//td'):
		#print td
		content = td.text_content().strip()
		# print td
		if content not in ["", "\\u00a0"]:
			row.append(content)
	row.append(year)
	row.append(agencyName)
	table.append(row)
print table