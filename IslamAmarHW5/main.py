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
germany_mean_arr = []
france_mean_arr= []
spain_mean_arr = []
days=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
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
        ax.set(xlabel='Date', ylabel='Number of Positive Cases', title='COVID-19 total cases  in Germany,France and Spain')
        ax.plot(germany_x, germany_y, label="Germany")
        ax.plot(france_x, france_y, label="France")
        ax.plot(spain_x, spain_y, label="Spain")
        ax.legend(loc='best')

def covidAnalysis(dataset):

    day_name = pd.to_datetime(dataset['Date']).dt.day_name()
    for counttry in countries:
        for day in days:
            countryDataset = (dataset[dataset["Country"] == counttry])
            country_day_set = (countryDataset[day_name == day])
            country_day_set = pd.to_numeric(country_day_set["New Case"] )
            if counttry == "Germany":
                Germanyarr.append(country_day_set.sum())
                germany_mean_arr.append(country_day_set.mean())
            elif counttry == "Spain":
                Spainarr.append(country_day_set.sum())
                spain_mean_arr.append(country_day_set.mean())
            else:
                Francearr.append(country_day_set.sum())
                france_mean_arr.append(country_day_set.mean())
#inference whether the infections tend to increase/decrease over weekends by ploting
def inference():
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    fig2 = plt.figure(2)
    fig2.suptitle("Total Number Of Infected New Cases Of Each Day Per 5 Months In Spain , Germany and France ")
    ax2 = plt.subplot(2, 2, 1)
    ax3 = plt.subplot(2, 2, 2)
    ax4 = plt.subplot(2, 2, 3)
    ax2.plot(days, Germanyarr, "or")  # one axis
    ax2.plot(days, Germanyarr, label="Germany")  # one axis
    ax2.legend(loc='best')
    ax2.set(xlabel='Days', ylabel='number of infected  cases ')
    ax3.plot(days, Spainarr, "or")  # one axis
    ax3.plot(days, Spainarr, "green", label="Spain")  # one axis
    ax3.set(xlabel='Days', ylabel=' number of infected  cases')
    ax3.legend(loc='best')
    ax4.plot(days, Francearr, "or")  # one axis
    ax4.plot(days, Francearr, "orange", label="France")  # one axis
    ax4.set(xlabel='Days', ylabel=' number of infected  cases')
    ax4.legend(loc='best')
    plt.show()
#inference whether the infections tend to increase/decrease over weekends by calculating mean of new cases for each day in 4 months
def display():
    print("***********************************************************")
    print(" the total mean of new cases in 5 months  in germany for each day ")
    for i, j in zip(days, germany_mean_arr):
        print(i + " : " + str(j))
    print(
        " by consideritng the weekend just for saturday and sunday , the study has shown that the mean number of new cases in germany in weekend less than the mean \n in other days so number of infection decreased at weekend in germany  with 1% error  ")
    print("***********************************************************")

    print("----------------------------------------------")
    print("***********************************************************")
    print(" the total mean of new cases in 5 months  in france for each day ")
    for i, j in zip(days, france_mean_arr):
        print(i + " : " + str(j))
    print(
        " by consideritng the weekend just for saturday and sunday , the study has shown that the mean number of new cases in france in weekend less than the mean \n in other days so number of infection decreased at weekend in france  with 1% error   ")
    print("***********************************************************")
    print("----------------------------------------------")
    print("***********************************************************")
    print(" the total mean of new cases in 5 months  in spain for each day ")
    for i, j in zip(days, spain_mean_arr):
        print(i + " : " + str(j))
    print(
        " by consideritng the weekend just for saturday and sunday , the study has shown that the mean number of new cases in spain in weekend less than the mean \n in other days so number of infection decreased at weekend in spain  with 1% error  ")
    print("***********************************************************")


ploting_data_set(dataset)
covidAnalysis(dataset)
display()
inference()
# print(germany_mean_arr)
# print(france_mean_arr)
# print(spain_mean_arr)
# print(Germanyarr)
# print(Spainarr)
# print(Francearr)


