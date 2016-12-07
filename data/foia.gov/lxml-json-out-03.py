from lxml import html
import requests
import json

page = requests.get('https://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2015&agencyName=USDA')
tree = html.fromstring(page.content)

row = tree.xpath('//table[@id="agencyInfo0"]/tr')
for td in rows:
	td = tree.xpath('//table[@id="agencyInfo0"]/tr/td/text()')
	print td

rows = []
for row in rows:
	row = tree.xpath('//table[@id="agencyInfo0"]/tr')
	print row
	rowCounter = 0
	rowCounter = rowCounter + 1
	print rowCounter
	for td in row:
		td = tree.xpath('//table[@id="agencyInfo0"]/tr/td/text()')
		print td
#showDateDay = tree.xpath('//span[@class="day"]/text()')
#showDateYear = tree.xpath('//span[@class="year"]/text()')
#showDate = tree.xpath('//span[@class="value-title"]/@title') #you want this title value

# get show headline
#showHeadline = tree.xpath('//div[@class="row contentBox visiblePrint"]/div/div/h2/a/text()')
# setListFMURL = "http://www.setlist.fm/"
# need to prepend this url in infront of showHeadlineSetListURL, as well as strip out leading "../" in the href attribute values...
#showHeadlineSetListURL = tree.xpath('//div[@class="row contentBox visiblePrint"]/div/div/h2/a/@href')

#showArtist = tree.xpath('//span[contains(text(),"Artist:")]/strong/a//span/text()')
#get venue value
#get setlist values
#get breadcrumbs values

# print 'Show Date Month: ', showDateMonth
"""
jsonOutputA = 'Show Date Month: ', showDateMonth
jsonOutputB = 'Show Date Day: ', showDateDay
jsonOutputC = 'Show Date Year: ', showDateYear
jsonOutputD = 'Show Date: ', showDate
jsonOutputE = 'Show Headline: ', showHeadline
jsonOutputF = 'Show Headline Setlist Link: ', showHeadlineSetListURL
jsonOutputG = 'Show Artist: ', showArtist

jsonOutput = '{', jsonOutputA ,'},{', jsonOutputB ,'},{', jsonOutputC ,'},{', jsonOutputD ,'},{', jsonOutputE ,'},{', jsonOutputF ,'},{', jsonOutputG ,'}'

with open('test-setlist-03.json', 'w') as outfile:
	json.dump(jsonOutput, outfile)"""