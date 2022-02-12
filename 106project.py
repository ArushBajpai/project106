import pandas as pd
import plotly.express as px
import numpy as np

data =pd.read_csv("coffee.csv")

fig = px.scatter(data,x = "Coffee in ml",y = "sleep in hours")
fig.show()

corr = np.corrcoef(data["Cofee in ml"],data["sleep in hours"])

print(corr)


data2 = pd.read_csv("students.csv")

fig2 = px.scatter(data2,x= "Days Present", y = "Marks In Percentage")
fig2.show()

corr2 = np.corrcoef(data2["Days Present"],data2["Marks In Percentage"])

print(corr2)
