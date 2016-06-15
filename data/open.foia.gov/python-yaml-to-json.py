import os
import sys
import yaml
import json


path = 'yamldata'
listing = os.listdir(path)
for infile in listing:
	print "current file is: " + infile
	json.dump(yaml.load(sys.stdin), sys.stdout, indent=4) < infile > infile + '.json'
