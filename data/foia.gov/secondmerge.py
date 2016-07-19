import os
import pandas as pd

filelist = []
methodlist = ["DataRequest","DataExemption","DataAppeal","DataProcessTime","DataFeewaiver","DataPerson","DataBacklog","DataConsultant","RequestDisposition","RequestDenial","RequestPending","Exemption3Statutes","appealDisposition","appealDenialEx","appealDenialOther","appealDenialReason","appealResponseTime","appeal10Pending","processingGranted","processingSimple","processingComplex","processingExpedited","processingPending","processing10Request","personnelCost","consultation10Oldest","requestCompare","requestBacklog","appealCompare","appealBacklog","feewaiverWaiver","DataPerson"]

def merge(method):
	files = [filename for filename in filelist if method in filename and csv in filename]
	return pd.concat((edit(f) for f in files) 
	

def edit(filename): #Takes filename, returns dataframe which can be aggregated.
	parts = filename.split("-")
	year = parts[0]
	agency = parts[1]
	tempdf = pd.read_csv(filename)
	tempdf.index = pd.Series(range(0, len(tempdf.index)))
	tempdf['Agency'] = pd.Series([agency for i in range(0, len(tempdf.index))]) #Add agency column
	tempdf['Year'] = pd.Series([year for i in range(0, len(tempdf.index))]) #Add year column
	return tempdf#[~tempdf.Component.str.contains(agency)] 


for method in methodlist:
	tempcsv = merge(method)
	tempcsv.to_csv(method + "full.csv")
