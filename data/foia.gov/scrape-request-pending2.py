from lxml import html
import requests
import json

page = requests.get('https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2015&agencyName=USPS')
tree = html.fromstring(page.content)

thead = ["Component", "Number Pending - Simple","Median No. of Days - Simple","Average No. of Days - Simple","Number Pending - Complex","Median No. of Days - Complex","Average No. of Days - Complex","Number Pending - Expedited","Median No. of Days - Expedited","Average No. of Days - Expedited","Year","Agency"]
year = 2015
agency = "USPS"

tableCellData = tree.xpath('//table/tbody/tr/td/center/span/text()')
print tableCellData

"""
tableRows = []
for tableRow in tableRows:
	tableCellData = tree.xpath('//table/tbody/tr/td/center/span/text()')
	print tableCellData
# print tableRows"""
"""
for tr in tree.xpath('//tr'):
	row = []
	for td in tr.xpath('//td'):
		content = td.text_content().strip()
		if content not in ["", "\\u00a0"]:
		# content = content + year
			row.append(content)
print row[0]"""
"""
jsonOutputA = 'Show Date Month: ', showDateMonth
jsonOutputB = 'Show Date Day: ', showDateDay
jsonOutputC = 'Show Date Year: ', showDateYear
jsonOutputD = 'Show Date: ', showDate
jsonOutputE = 'Show Headline: ', showHeadline
jsonOutputF = 'Show Headline Setlist Link: ', showHeadlineSetListURL
jsonOutputG = 'Show Artist: ', showArtist
jsonOutputH = 'Show Tour: ', showTour
jsonOutputI = 'Show Venue: ', showVenue
jsonOutputJ = 'Show Setlist: ', showSetList
jsonOutputK = 'Go to Last Page Value: ', showTotalDocuments # definitely don't need this in json
jsonOutputL = 'String Variable Concatenation #02: ', veneuShowsResultsURL + str(showTotalDocuments)


jsonOutput = '{', jsonOutputA ,'},{', jsonOutputB ,'},{', jsonOutputC ,'},{', jsonOutputD ,'},{', jsonOutputE ,'},{', jsonOutputF ,'},{', jsonOutputG ,'},{', jsonOutputH ,'},{', jsonOutputI ,'},{', jsonOutputJ ,'},{', jsonOutputK ,'},{', jsonOutputL ,'}'

with open('setlist-07.json', 'w') as outfile:
	json.dump(jsonOutput, outfile)"""