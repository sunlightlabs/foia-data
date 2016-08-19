# //Abbreviation of agencies
# agenciesAb[,'ALL'
from lxml import html
import requests
import json



foiaGovAgencies = ['USDA','DOC','DoD','ED','DOE','HHS','DHS','HUD','DOI','DOJ','U.S. DOL','State','DOT','Treasury','VA','ACUS','USAID','ABMC','NRPC','AFRH','BBG','CIA','CSB','USCCR','CPPBSD','CFTC','CFPB','U.S. CPSC','CNCS','CIGIE','CSOSA','DNFSB','EPA','EEOC','CEQ','OMB','ONDCP','OSTP','USTR','Ex-Im Bank','FCA','FCSIC','FCC','FDIC','FEC','FERC','FFIEC','FHFA','FLRA','FMC','FMCS','FMSHRC','FOMC','FRB','FRTIB','FTC','GSA','IMLS','IAF','LSC','MSPB','MCC','NASA','NARA','NCPC','NCUA','NEA','NEH','NIGC','NLRB','NMB','NSF','NTSB','USNRC','OSHRC','OGE','ONHIR','OPM','OSC','ODNI','OPIC','PC','PBGC','PRC','PCLOB','RATB','US RRB','SEC','SSS','SBA','SSA','SIGAR','SIGIR','STB','TVA','USAB','US ADF','CO','USIBWC','USITC','USPS','USTDA']
foiaGovYearsPrefix = "requestYear="
foiaGovYears = ['2008','2009','2010','2011','2012','2013','2014','2015']

for govAgency in foiaGovAgencies:
	print "This is foia.gov Agency of type: %s" % govAgency


foiaDotGovURLPath = "http://www.foia.gov/foia/Services/processingSimple.jsp?"
foiaDotGovURLYears = "requestYear=2008&requestYear=2009&requestYear=2010&requestYear=2011&requestYear=2012&requestYear=2013&requestYear=2014&requestYear=2015"
foiaDotGovURLAgencyAPI = "&agencyName="

# foiaDotGovURLScrape = foiaDotGovURLPath + foiaDotGovURLYears + foiaDotGovURLAgencyAPI + foiaGovAgencies[0]
foiaDotGovURLScrape = foiaDotGovURLPath + foiaGovYearsPrefix + foiaGovYears[0] + foiaGovAgencies[0]

print 'foia.gov URL to be scraped: ', foiaDotGovURLScrape