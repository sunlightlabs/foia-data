from urllib2 import urlopen
import lxml.html
import requests
import json
import csv

page = requests.get('https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2015&agencyName=USPS')
tree = lxml.html.parse(page.content)

table = tree.xpath('//table/tbody/')

print table



"""
url = requests.get('https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2015&agencyName=USPS')
html = lxml.html.document_fromstring(r.text)
rows = html.xpath(xpath1)[0].findall("tr")

data = list()
table = []

for rows in table:
	tableCellData = tree.xpath('//table/tbody/tr/td/text()')
	table.append(tableCellData)
	print tableCellData
print table

xpath1 = "tbody/tr"
r = requests.post(url,data)
html = lxml.html.fromstring(r.text)
rows = html.xpath(xpath1)
data = list()
for row in rows:
    data.append([c.text for c in row.getchildren()])"""