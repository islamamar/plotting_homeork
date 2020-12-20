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
countries =["Germany","Spain","France"]
# Ploting the number of infections over several months in 3-4 European countries
def ploting_data_set(dataset):

        Geramnyset = (dataset[dataset["Country"] == "Germany"])
        germany_x = pd.to_datetime(Geramnyset['Date'])
        germany_y= pd.to_numeric(Geramnyset['Total Case'])

        Spainset = (dataset[dataset["Country"] == "Spain"])
        spain_x = pd.to_datetime(Spainset['Date'])
        spain_y = pd.to_numeric(Spainset['Total Case'])

        Franceset =(dataset[dataset["Country"] == "France"])
        france_x = pd.to_datetime(Franceset['Date'])
        france_y = pd.to_numeric(Franceset['Total Case'])

        fig, ax = plt.subplots()  # one axis
        ax.set(xlabel='Date', ylabel='Number of Positive Cases', title='COVID-19 total cases  in Germany,United Kingdom and Spain')
        ax.plot(germany_x, germany_y, label="Germany")
        ax.plot(france_x, france_y, label="France")
        ax.plot(spain_x, spain_y, label="Spain")
        ax.legend(loc='best')
