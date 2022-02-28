import csv

with open('class1.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove the headers
file_data.pop(0)

sum = 0
n = len(file_data)

#int, decimals included in float
for i in file_data:
    sum = sum + float(i[1])


mean = sum/n
print(mean)

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df, x = "Student Number", y = "Marks")

fig.update_layout(shapes = [dict(
    type = 'line',
    y0 = mean, y1 = mean,
    x0 = 0, x1 = n
)])

fig.update_yaxes(rangemode = "tozero")
fig.show()

