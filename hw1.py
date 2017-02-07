import csv
csvfile2 = open('source/data/chp3/data-text.csv', 'rb');
reader2 = csv.DictReader(csvfile2)
for row2 in reader2:
	print row2