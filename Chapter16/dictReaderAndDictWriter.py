#use for csv files with header rows
#it uses dictionaries instead of list

import csv
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    #Timestamp, Fruit, Quantity are the headers (keys)
    print(row['Timestamp'], row['Fruit'], row['Quantity'])


#we could also add headers ourselves, for example
#if we use example.csv with no headers, we can do:
exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',
'amount'])
for row in exampleDictReader:
    #Timestamp, Fruit, Quantity are the headers (keys)
    print(row['time'], row['name'], row['amount'])


#if you want your csv to contain a header row, write that row
#by calling writeheader

outputFile = open('output2.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone':'555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':
'dog'})
outputFile.close()
