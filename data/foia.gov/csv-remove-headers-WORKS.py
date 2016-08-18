import csv, os

# create directory to place csvs with new headers
os.makedirs('processingGrantedEdited')
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
	csvRows = []
	# header row we need to add - NOTE: the blank ',""' at end of this headers array is necessary as all of the csvs have the delimiting comma ending each line
	newCSVHeaderRow = ["Component","Simple - Median No. of Days","Simple - Average No. of Days","Simple - Lowest No. of Days","Simple - Highest No. of Days","Complex - Median No. of Days","Complex - Average No. of Days","Complex - Lowest No. of Days","Complex - Highest No. of Days","Expedited - Median No. of Days","Expedited - Average No. of Days","Expedited - Lowest No. of Days","Expedited - Highest No. of Days",""]
	csvRows.append(newCSVHeaderRow)
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num < 3: # this example has two rows of headers; both need to be swapped out.
			continue
		csvRows.append(row)
	csvFileObj.close()
	csvFileObj = open(os.path.join('processingGrantedEdited', csvFilename), 'w')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()

	print('Removing Header from ' + csvFilename + '...')