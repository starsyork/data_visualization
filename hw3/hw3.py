from pdftables import get_tables
import pprint

headers = ['Site','Parameter','Date (LST)','Year','Month','Day','Hour','Value','Unit','Duration','QC Name']

all_tables = get_tables(open('AQI_2016_11.pdf', 'rb'))

first_name = False
data = []

#Get headers and row for PDF file
for table in all_tables:
    for row in table[5:]:
        data.append(dict(zip(headers, row)))

#Pare dict and build a new dict
final_data = []
for ele in data:
    #Jump off unvalid data
    if ele.get('QC Name') == 'Missing':
        continue
    site = ele.get('Site')
    del ele['Site']
    
    final_data.append({site:ele})
    
pprint.pprint(final_data)
