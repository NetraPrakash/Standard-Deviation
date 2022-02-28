import csv
with open('class2.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

sum= 0
n=len(file_data)


#add the new row of marks, increasing value each time - incrementation
for i in file_data:
    sum=sum+float(i[1])
    
mean=sum/n
print(mean)

import pandas as pd
import plotly.express as px

df=pd.read_csv('class2.csv')

fig=px.scatter(df, x="Student Number", y="Marks")

fig.update_layout(shapes=[dict(type='line', y0=mean, y1=mean, x0=0, x1=n)])
fig.update_yaxes(rangemode='tozero')
fig.show()
