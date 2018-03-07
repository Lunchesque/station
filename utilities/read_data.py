import csv

def getCSVData(fileName):
    #Create an empty list to store rows
    rows = []
    #Open the CSV file
    dataFile = open(fileName, "r")
    #Create reader for data in CSV file
    reader = csv.reader(dataFile)
    #skip the headers
    next(reader)
    #add row from reader to list
    for row in reader:
        rows.append(row)
    return rows
