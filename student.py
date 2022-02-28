import csv

with open('student.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data=file_data[0]


def mean(data):
    sum = 0
    n = len(data)

    #int, decimals included in float
    for i in data:
        sum = sum + int(i)

    mean = sum/n
    print(mean)
    return mean

squarelist=[]
for i in data:
    difference=int(i)-mean(data)
    #print(difference)
    difference=difference**2
    squarelist.append(difference)

squaresum=0
for i in squarelist:
    squaresum=squaresum+i

result=squaresum/(len(data)-1)
print(result)
import math
standarddeviation=math.sqrt(result)
print(standarddeviation)

