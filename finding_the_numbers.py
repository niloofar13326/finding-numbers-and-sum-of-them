import re 
fh=open('regex_sum.txt')
finding_numbers=[]
for line in fh:
    line=line.rstrip()
    finding_numbers=re.findall('([0-9]+)',line)+finding_numbers
sumofnum=0
for num in finding_numbers:
    sumofnum=int(num)+sumofnum
print(sumofnum)