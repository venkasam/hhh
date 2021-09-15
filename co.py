import plotly.express as px
import csv

with open("data1.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df ,x="Coffeeml",y="sleep")
    fig.show()
    


