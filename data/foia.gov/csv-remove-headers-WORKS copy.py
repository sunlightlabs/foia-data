import csv, os

# create directory to place csvs with new headers
os.makedirs('requestCompareEdited')
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
	csvRows = []
	# header row we need to add - NOTE: the blank ',""' at end of this headers array is necessary as all of the csvs have the delimiting comma ending each line
	newCSVHeaderRow = ["Component","Number of Requests Received - Number of Received During Fiscal Year From Last Year's Annual Report","Number of Requests Received - Number of Received During Fiscal Year From Last Year's Curren Report","Number of Requests Processed - Number of Received During Fiscal Year From Last Year's Annual Report","Number of Requests Processed - Number of Received During Fiscal Year From Last Year's Current Report",""]
	csvRows.append(newCSVHeaderRow)
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num < 3: # this example has two rows of headers; both need to be swapped out.
			continue
		csvRows.append(row)
	csvFileObj.close()
	csvFileObj = open(os.path.join('requestCompareEdited', csvFilename), 'w')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

	print('Removing Header from ' + csvFilename + '...')