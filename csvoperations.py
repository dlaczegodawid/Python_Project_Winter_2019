import os
import glob
import csv
import pandas as pd
path = 'C:/Users/Dawid/Documents/csv'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
print(result)

for file_name in result:
    with open(file_name, 'r') as csvinput:
        with open(file_name, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('Berry')
            all.append(row)

            for row in reader:
                row.append(row[0])
                all.append(row)

            writer.writerows(all)


