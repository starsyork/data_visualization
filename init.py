import csv
Shenyang = csv.DictReader(open('source/Shenyang.csv', 'rb'))
Beijing = csv.DictReader(open('source/Beijing.csv', 'rb'))
Shanghai = csv.DictReader(open('source/Shanghai.csv', 'rb'))
Chengdu = csv.DictReader(open('source/Chengdu.csv', 'rb'))
Guangzhou = csv.DictReader(open('source/Guangzhou.csv', 'rb'))

for row in Shenyang:
	print row['Site']+"  "+row['Date (LST)']+ "  AQI: " + row['Value']
for row in Beijing:
	print row['Site']+"  "+row['Date (LST)']+ "  AQI: " + row['Value']
for row in Shanghai:
	print row['Site']+"  "+row['Date (LST)']+ "  AQI: " + row['Value']
for row in Chengdu:
	print row['Site']+"  "+row['Date (LST)']+ "  AQI: " + row['Value']
for row in Guangzhou:
	print row['Site']+"  "+row['Date (LST)']+ "  AQI: " + row['Value']