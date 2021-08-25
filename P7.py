import pandas as pd
import plotly.express as pe
data=pd.read_csv("Copy+of+data+-+data.csv")
fig=pe.scatter(data,x="date",y="cases",color="country")
fig.show()