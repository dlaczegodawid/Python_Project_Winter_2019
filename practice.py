import os
import glob

path = 'C:/Users/Dawid/Documents/csv'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
print(result)

# importing csv module
import csv

# csv file name


with open("IBM.csv","r", ) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[2])



