x = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
for i in x:
	print i


years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
for year in years:
	print year






# http://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2014&requestYear=2015&agencyName=LSC&agencyName=FDIC&agencyName=USPS&Random=195

urlA = "http://www.foia.gov/foia/Services/processingSimple.jsp?requestYear="
urlB = ["2008", "2009", "2010", "2012", "2013", "2014", "2015"]
# urlB = "2015"
urlC = "&agencyName="
urlD = "LSC"

for year in urlB:
	ano = 0
	urlScrape = urlA + urlB[ano] + urlC + urlD
	++ano
	print urlScrape

