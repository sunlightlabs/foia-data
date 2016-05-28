import lxml.html as LH
import requests
import json

tree = LH.parse("http://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2014&agencyName=FDIC")

# print([th.text_content() for th in tree.xpath('//th')])
# print([td.text_content() for td in tree.xpath('//td')])

tableHead = ([th.text_content() for th in tree.xpath('//th')])
tableBody = ([td.text_content() for td in tree.xpath('//td')])
tableData = tableHead + tableBody
print tableData

with open('2014-FDIC.json', 'w') as outfile:
	json.dump(tableData, outfile)