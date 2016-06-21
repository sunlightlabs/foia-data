import os
import pandas as pd

os.chdir("csv") #Start in "csv" folder containing all the .txt files.
filenames = os.listdir(os.getcwd())


def goodfile(f): #Returns if the file should be concatenated with the rest or not.
	print(f)
	if len(f.split("-")) > 2 and "Ex" not in f: #Excludes the summary files from merging (files of the form CFPB-2008-2015), which duplicate all the info. Exception for the Ex-Im Bank.
		#print("Badfile: " + f)
		return False
	tempdf = pd.read_csv(f)
	if len(tempdf.columns) != 15:
		#print("BadCols: " + f)
		return False
	return True

def edit(filename): #Takes filename, returns dataframe which can be aggregated.
	parts = filename.split("-")
	agency =  parts[0] #Files have form Agency-Year.
	year = parts[1].split(".")[0]
	tempdf = pd.read_csv(filename)
	tempdf.index = pd.Series(range(0, len(tempdf.index)))
	tempdf['Agency'] = pd.Series([agency for i in range(0, len(tempdf.index))]) #Add agency column
	tempdf['Year'] = pd.Series([year for i in range(0, len(tempdf.index))]) #Add year column
	return tempdf#[~tempdf.Component.str.contains(agency)] 
	


mydf = pd.concat((edit(f) for f in sorted(filenames) if goodfile(f) == True)) 
mydf = mydf[mydf.Component != mydf.Agency] #Removes rows in which an agency appears twice in the data, first as itself, then as a "Total" column with all the same information.
mydf.to_csv("fulldata.csv")
