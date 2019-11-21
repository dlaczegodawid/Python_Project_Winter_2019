import os
import glob

path = 'C:/Users/Dawid/Documents/csv'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
print(result)



import pandas as pd



for filename in result:
    df = pd.read_csv(filename, sep=',')
    df["Changes"]= (df['Close']-df['Open'])/df['Open']
    f = open(filename, "w+")
    f.close()
    df.to_csv(filename)
    print(df["Changes"])



