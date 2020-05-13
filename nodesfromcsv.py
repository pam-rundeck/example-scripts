import csv
import sys
import codecs

f = sys.argv[1] 

with open(f, 'r') as csvfile:
	reader = csv.DictReader(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig'), dialect='excel')
	for row in reader:
		print row
