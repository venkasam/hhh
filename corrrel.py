import csv
import plotly.express as px 
import numpy as np

def getsource(datapath):
    ice=[]
    cold=[]
    with open(datapath) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            ice.append(float(row["SizeTV"]))
            cold.append(float(row["Average"]))
    return {"x":ice,"y":cold}

def corr(datasource):
    corrrel=np.corrcoef(datasource["x"],datasource["y"])
    print("corrrelation betwwen temprature and iceacream:",corrrel[0,1])


def main():
    datapath="data1.csv"
    datasource=getsource(datapath)
    corr(datasource)
    
main()
with open("data1.csv") as f:
 csv_reader=csv.DictReader(f)
 a=px.scatter(csv_reader,x="SizeTV",y="Average")
 a.show()