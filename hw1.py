# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '109061113.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data: remove data with the value of WDSD being '-99.000' or '-999.000'

for i in data:
    if i['WDSD'] == '-99.000' or i['WDSD'] == '-999.000':
        data.remove(i)

# Retrive needed data points.
# record data amounts, maximum and minimum value of WDSD of each station

target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
M = 0       # max
m = 0       # min
amount = 0  # data amount
for i in target_data:
    if float(i['WDSD']) > float(M):
        M = i['WDSD']
    elif float(i['WDSD']) < float(m):
        m = i['WDSD']
    amount += 1
if amount <= 1:
    result = [['C0X260', 'None']]
else:    
    result = [['C0X260', float(M) - float(m)]]

target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
M = 0       # max
m = 0       # min
amount = 0  # data amount
for i in target_data:
    if float(i['WDSD']) > float(M):
        M = i['WDSD']
    elif float(i['WDSD']) < float(m):
        m = i['WDSD']
    amount += 1
if amount <= 1:
    result.append(['C0R190', 'None'])
else:    
    result.append(['C0R190', float(M) - float(m)])

target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
M = 0       # max
m = 0       # min
amount = 0  # data amount
for i in target_data:
    if float(i['WDSD']) > float(M):
        M = i['WDSD']
    elif float(i['WDSD']) < float(m):
        m = i['WDSD']
    amount += 1
if amount <= 1:
    result.append(['C0G640', 'None'])
else:    
    result.append(['C0G640', float(M) - float(m)])

target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
M = float(0)       # max
m = float(0)       # min
amount = 0  # data amount
for i in target_data:
    if float(i['WDSD']) > float(M):
        M = i['WDSD']
    elif float(i['WDSD']) < float(m):
        m = i['WDSD']
    amount += 1
if amount <= 1:
    result.append(['C0F9A0', 'None'])
else:    
    result.append(['C0F9A0', float(M) - float(m)])

target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
M = 0       # max
m = 0       # min
amount = 0  # data amount
for i in target_data:
    if float(i['WDSD']) > float(M):
        M = i['WDSD']
    elif float(i['WDSD']) < float(m):
        m = i['WDSD']
    amount += 1
if amount <= 1:
    result.append(['C0A880', 'None'])
else:    
    result.append(['C0A880', float(M) - float(m)])



#=======================================


# Part. 4

#=======================================

# Print result

result.sort(key = lambda l: l[0])
print(result)

#========================================
