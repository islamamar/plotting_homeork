import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("D:/book/python/COVID-19_Data_Europe.csv",sep = ',')
newdataset  = dataset[["Date","Country","Total Case"]]
year = dataset["Date"]
date = pd.to_datetime(year)
print(date)
print(type(date))
print(type(year))
Germanyarr=[]
Spainarr = []
Francearr = []
germany_x=[]
germany_y = []
spain_x =[]
spain_y =  []
france_x = []
france_y =  []