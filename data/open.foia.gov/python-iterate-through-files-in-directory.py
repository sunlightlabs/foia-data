import os

path = 'yamldata'
listing = os.listdir(path)
for infile in listing:
	print "current file is: " + infile