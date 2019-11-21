import os
#print(os.getcwd())

#f.path = r'h:\test\run.m'

#with open(f_path, "r") as in_f:
#    for line in in_f.readlines():
#        print(line)

#def countBalls(n):
#    k=0
#    x=1
#    while(n>k):
#        nx+n
#    print(x)

#countBalls(5)

def sum_row(row):
    if row==1:
        return 1
    else:
        return sum_row(row-1)+row
print(sum_row(5))

#sum of the size
#if sth is file
#if sth is directory

import os
dir = 'C:\\'
files = os.listdir(dir)
#print(files)

for f in files:
    if os.path.isdir(os.path.join(dir, f)):
        print('dir' + f)
    else:
        print('file' + f + str(os.path.getsize(os.path.join(dir, f))))



