# [foia.gov](https://www.foia.gov/)  

## [FOIA.gov Data Options Offered/Not Offered](https://www.foia.gov/data.html) 
### Report Category: Fee Waive  
Requests ** As far as I can tell, feewaiverWaiver is still exposed/functional, the option above it in the HTML serves the same purpose. Or rather, the commented out option is a feature, and not an option.  

### Advanced Report Categories  
![Screenshot of Cluttered UI for Advanced Search on foia.gov](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/broken-ui.png)  
Denial  
Exemption 3 Statutes - Available under Basic Search -> Exemptions -> Exemption 3 Statutes [Exemption 3 Statutes - USDA 2015](https://www.foia.gov/foia/Services/Exemption3Statutes.jsp?requestYear=2015&agencyName=USDA)  
Denials(Reasons)  
Appeals Denials (Reasons) Available under Basic -> Appeals - Dis. "Other" Reasons [Appeal Denials (Reasons) - DOJ 2015](https://www.foia.gov/foia/Services/appealDenialReason.jsp?requestYear=2015&agencyName=DOJ)  
Is actually available from basic search under Appeals - Dis. - "Other" Reasons  
Ten Oldest Consultations - Available from Basic Search -> Consultations - Ten Oldest
[Ten Oldest Consultations - USDA 2010](https://www.foia.gov/foia/Services/consultation10Oldest.jsp?requestYear=2010&agencyName=USDA)  
Confusing - look at -> [Ten Oldest Consultations from USDA 2008](https://www.foia.gov/foia/Services/consultation10Oldest.jsp?requestYear=2008&agencyName=USDA)  
Zero answers in 2008, yet 2010 has a consultation from 2008.  
Comparisons  
  Comparisons - Available under Basic -> Comparisons
  [Comparisons (Requests Compare) - USDA 2010](https://www.foia.gov/foia/Services/requestCompare.jsp?requestYear=2010&agencyName=USDA)  
  Backlogged - Available under Basic -> Comparisons -> Reports Backlogged  
  [Requests Backlog - USDA 2010](https://www.foia.gov/foia/Services/requestBacklog.jsp?requestYear=2010&agencyName=USDA) 
  Administrative Appeals - Available under Basic -> Comparisons -> Administrative Appeals  
  [Appeals Compare - USDA 2010](https://www.foia.gov/foia/Services/appealCompare.jsp?requestYear=2010&agencyName=USDA)  
  Appeals Backlogged - Availalbe under Basic -> Comparisons -> Appeals Compare  
  [Appeals Backlog - USDA 2010](https://www.foia.gov/foia/Services/appealBacklog.jsp?requestYear=2010&agencyName=USDA)
  [Backlog Option Available from Basic Search - USDA 2010](https://www.foia.gov/foia/Services/DataBacklog.jsp?requestYear=2010&agencyName=USDA)  
  Backlog Requests are confusing from Advanced Search  
  Compare below image from Advanced Search - Advanced Search -> Backlog -> USDA (Department of Agriculture) -> 2010:  
![Basic Search Advanced Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/backlog-requests-and-repairs-usda-2010.png)    
  Compare Backlog Requests from Basic Search:  
![Backlog Search Basic Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/backlog-search-basic.png)  
[Request Backlog API Call - Not the same results as either: foia.gov/foia/Services/requestBacklog.jsp?requestYear=2010&agencyName=USDA](https://www.foia.gov/foia/Services/requestBacklog.jsp?requestYear=2010&agencyName=USDA)  
Not even the same agency names, etc.  
![Request Backlog Results API Call Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/request-backlog-api-call-results.png)   

### Requests - Denied and Pending
![Requests Denial Commented Out Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/fail-foia.gov-reports-options-not-offered-02.png)  

These are still exposed via breadcrumbs in the basic search page but that is the only place I can find that functionality:  
Denial  
[Requests Denied - USDA 2015](https://www.foia.gov/foia/Services/RequestDenial.jsp?requestYear=2015&agencyName=USDA)  
Pending  
[Requests Pending - USDA 2015](https://www.foia.gov/foia/Services/RequestPending.jsp?requestYear=2015&agencyName=USDA)  

## Advanced Report Options - Available  
reportRequests      Report Name ->Requests  
requestDisposition      Report Name ->   - Disposition  
reportFeeWaiver      Report Name ->   - Expedited Processing  
reportExemptions      Report Name -> Exemptions  
reportAppeals      Report Name -> Appeals  
appealDisposition      Report Name ->   - Disposition (Dis.)  
appealDenialEx      Report Name ->   - Dis. Use of Exemptions  
appealDenialOther      Report Name ->   - Dis. Other Than Exemptions  
appealResponseTime      Report Name ->   - Response Time  
appeal10Pending      Report Name ->   - Ten Oldest Pending  
reportProcessingTime      Report Name -> Processing Time  
processingGranted      Report Name ->   - Requests Granted  
processingSimple      Report Name ->   - Simple Requests  
processingComplex      Report Name ->   - Complex Requests  
processingExpedited      Report Name ->   - Expedited Requests  
processingPending      Report Name ->   - Pending Requests  
processing10Request      Report Name ->   - Ten Oldest Requests  
feewaiverWaiver      Report Name -> Fee Waiver  
reportPersonnel      Report Name -> Administration  
personnelCost      Report Name ->   - FOIA Costs  
reportBacklog      Report Name -> Backlog  
reportConsultations      Report Name -> Consultations  

### Advanced Report Options - Not Available/Visible to Users  
HTML Options Commented Out Screenshot  
![HTML Options Commented Out Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/basic-search-option-elements-commented-out-markup-foia.gov-screenshot.png)  
Closer Version of HTML Options Commented Out Screenshot
![Closer Version of HTML Options Commented Out Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/commented-out-markup-options.png)  

requestDenial      Report Name ->   - Denial  
Exemption3Statutes      Report Name ->   - Exemption 3 Statutes  
appealDenialReason      Report Name ->   - Denials(Reasons)  
consultation10Oldest      Report Name ->   - Ten Oldest  
requestCompare      Report Name ->   - Comparisons  
requestBacklog      Report Name ->   - Backlogged  
appealCompare      Report Name ->   - Administrative Appeals  
appealBacklog      Report Name ->   - Appeals Backlogged  

RSS feed hasn't been updated since 2011:
[FOIA RSS - 2011-09-06](https://www.foia.gov/xml/foiarss.xml)  
[News Spotlight - cobwebs](https://www.foia.gov/news-spotlight.html)  
[News Archive is Maintained](https://www.foia.gov/news-archive.html)  
[And Provides New/Maintained RSS Feed](https://www.foia.gov/iso/opa/foia/foiarss.xml)  

Sitemap  
[Sitemap](https://www.foia.gov/sitemap.html)  
Missing Documents:  
[Spanish Index](https://www.foia.gov/index-es.html)  
[Report - Make Request](https://www.foia.gov/report-makerequest.html)  
[Search](https://www.foia.gov/search.html)  
From Sitemap -> Click on News Spotlight -> Click on RSS Icon top right -> takes you to feed last updated 2011-09-06
[old feed from sitemap](https://www.foia.gov/xml/foiarss.xml)  





  
## Simple vs. Advanced Requests  
Basic Request - USDA 2010  
Basic Request - USDA 2010 Screenshot  
![Basic Request - USDA 2010](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/simple-requests-screenshot.png)  
Advanced Request - USDA 2010 Screenshot  
![Advanced Request - USDA 2010](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/advanced-request-screenshot.png)   

## Processing Times: Simple Requests vs. Complex Requests
[Simple Requests](https://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2010&agencyName=USDA&Random=183)  
[Complex Requests](https://www.foia.gov/foia/Services/processingComplex.jsp?requestYear=2010&agencyName=USDA&Random=45)  
[Processing Simple Requests Full](https://github.com/sunlightlabs/foia-data/blob/master/data/foia.gov/full/processingSimple-2008-2015.csv)  
[Processing Complex Requests Full](https://github.com/sunlightlabs/foia-data/blob/master/data/foia.gov/full/processingComplex-2008-2015.csv)  
[D3 Chart - Processing Simple Requests Full - Totals](http://dev.bowdenweb.com/processing-times-simple.html)  
[D3 Chart - Processing Complex Requests Full - Totals](http://dev.bowdenweb.com/processing-times-complex.html)  

## Options Not Being Offered/Bad UI/UX  
Featured Option Not Being Offered  
![Featured Option Not Being Offered](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/featured-option-not-being-offered.png)  
Learn How to Make a Basic FOIA Report Not Being Offered  
![Learn How to Make a Basic FOIA Report Not Being Offered](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/learn-how-to-make-a-basic-foia-report-not-being-offered.png)  
Odd/Confusing  
![Odd/Confusing](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/useless.png)  
View More Data Options Commented Out  
![View More Data Options Commented Out](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/view-more-data-options-not-being-offered.png)  
foia.gov Alert Fail  
![foia.gov Alert Fail](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/fail-foia.gov-css-error-and-alert-error-yay.png)  
foia.gov Select Components Screenshot  
![foia.gov Select Components Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/fail-foia.gov-data-advanced-report-select-components-chrome.png)  
foia.gov View Video in Firefox Screenshot  
![foia.gov View Video in Firefox Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/fail-foia.gov-data-video-firefox.png)  
Misspelling of Exemption Screenshot  
![Misspelling of Exemption Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/mispelling.png)  
Sitemap Last Updated 2011 Screenshot  
![Sitemap Last Updated 2011 Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/sitemap-last-updated-2011.png)  

# Takeaways  
Why is Basic more advanced than Advanced?  
Why are the Denials not provided at all?  
Why are some of the options only provided via breadcrumbs (not really provided, you have to be inspecting/paying attention)?  
What is the difference between foia.gov vs. foiaonline.regulations.gov?  
Why is foia.gov partially/poorly maintained?  
Why are their different results shown for the three backlog requests searches?  
We could build a better search [Build Better Search via Proxy](http://dev.bowdenweb.com/proxy-foia-demo.html)  
We could serve up better results [Search Results via Proxy](http://dev.bowdenweb.com/proxy-foia-jsp-results.html)  
[Compared to Search Results API](https://www.foia.gov/foia/Services/processingSimple.jsp?requestYear=2015&agencyName=USDA)  
We could fork JKAN and host foia data we've scraped in it on github  

# OTHER FOIA SITES  

## OGIS  
Nonvalid CSV - OGIS FOIA CSV Download Screenshot in Open Office  
![OGIS FOIA CSV Download Screenshot in Open Office](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/ogis-csv-download-rendering-in-openoffice-2016-05-26.png)  
OGIS Library RSS Feed - Check Last Update (2011-11-28)  
[OGIS Library RSS Feed - Check Last Update (2011-11-28)](https://ogis.archives.gov/Page298_Topic8.rss)  
OGIS Events and Presentation Calendar Screenshot  
[OGIS Events and Presentation Calendar](https://ogis.archives.gov/Page298_Topic7.rss)  

## 18f/open.foia.gov
[Where/How Does open.foia.gov Fit Into The Mix?](https://open.foia.gov/)  
[18f open.foia.gov Looks A Little Abandoned](http://foia-hub.readthedocs.io/en/latest/api.html)  
[github - last updated 7 months ago](https://github.com/18F/foia-hub)  

## foiaonline.regulations.gov  
[Down to the details of design, not sure what the difference(s) Are between foia.gov and foiaonline.regulations.gov](https://foiaonline.regulations.gov/foia/action/public/report)  
Definitely offers Denials Report(s):  
foiaonline.regulations.gov FOIA Denial Report Screenshot  
![foiaonline.regulations.gov FOIA Denial Report Screenshot](https://raw.githubusercontent.com/sunlightlabs/foia-data/master/screen-shots/foiaonline.regulations.gov-partial-denials-search.png)  




