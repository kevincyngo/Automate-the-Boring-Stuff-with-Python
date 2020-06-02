import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)

# print(*exampleData, sep='\n')

# for larger files, read data using a for loop
# this avoids loading the entire file into memory at once
# Note the reader object can be looped over only once, to re read the csv
# you need to call csv.reader to create another reader object
for row in exampleReader:
    print('Row#'+str(exampleReader.line_num)+" "+str(row))
