# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:50:21 2020

@author: Snoopy
"""

import numpy as np
import os
import sys
os.environ['PROJ_LIB'] = r'C:\Users\Snoopy\Installs\Anaconda\pkgs\proj4-5.2.0-ha925a31_1\Library\share'
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import datetime
import webbrowser
import gmplot
#import plotly as py
#import plotly.express as px
#import plotly.graph_objs as go
#from plotly.subplots import make_subplots
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)

def getvirus(): #opens website and writes data to a file
      
        month=input("Enter the month as 02 for February, 03 for March.... :")
        day=input("Enter the day as a 2 digit number for each month: ")
        year=input("Enter the 4 digit year: ")
        try:
           webaddress=f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{day}-{year}.csv"
           url = webaddress
           df=pd.read_csv(url)
           df.columns=['Province','Country', 'Updated', 'Confirmed','Deaths','Recovered','Lat','Long']
           df.sort_values('Country', ascending=True, inplace=True)
        
           #code can be activated to print the raw pandas dataframe
        
           #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
             #        print(df)
        
           df = df[df['Confirmed']>0] 
           df.to_csv('c:\pythonprograms\Coronavirus\coronadata2.csv', index=False)
        except:
            print("ERROR IN URL, RE-ENTER MONTH/DAY/YEAR\n")
            sys.exit()
        else:
            pass
        
    
def plotmap(df):
    
       lat = df['Lat'].values
       lon = df['Long'].values
       plt.figure(figsize=(16,12))
       m = Basemap(projection='robin',lon_0=-70., lat_0=20., width=20000000, height=10000000,
            resolution ='h')
       m.drawcoastlines()
       m.drawcountries()
       m.drawmapboundary(fill_color='#99ffff')
       m.fillcontinents(color='#cc9966',lake_color='#99ffff', zorder=5)
       m.drawparallels(np.arange(-90.,120.,30.))
       m.drawmeridians(np.arange(0.,360.,30.))
       title="Coronavirus Map"
       plt.title(title)
       plt.tight_layout()
       lons, lats = m(lon,lat)
       # plot points as red dots
       m.scatter(lons, lats, marker = 'o', color='r', zorder=5)
       plt.pause(0.5)
       plt.show()
       
       
def graphcases(df):
    width=0.25
    plt.figure(figsize=(16,12))
    plt.ylim(0,4000)
    plt.rcParams['axes.facecolor'] = 'gray'
    plt.xticks(rotation=90)
    plt.bar(df['Country'], df['Confirmed'], width, color='blue', label='Confirmed Cases')
    plt.bar(df['Country'], df['Deaths'], width, color='red', label='Deaths')
    plt.xlabel("Country of Origin")
    plt.ylabel("COVID19 Cases")
    titlestring="Chart of COVID19 by Country" + " Date " +  str(datetime.datetime.now())
    plt.title(titlestring)
    plt.legend(loc='right')
    plt.show() 
    
def datatable(df):
     df_table = pd.DataFrame({'Province': df['Province'],'Country': df['Country'], 'Cases': df['Confirmed'],'Deaths': df['Deaths']})

     #render dataframe as html
     html = df_table.to_html()

     #write html to file
     text_file = open("Coronavirusdata.html", "w")
     text_file.write(html)
     text_file.close()
     webbrowser.open('Coronavirusdata.html', new=2)
     
def heatmap(df):
    
    lats= df["Lat"]
    lons = df["Long"]

    # Creating the location we would like to initialize the focus on. 
    # Parameters: Lattitude, Longitude, Zoom
    gmap = gmplot.GoogleMapPlotter(30.5, -81.5,1, apikey="AIzaSyC-92qDWE-L9OnJY_YFG3s2QZ7LRRRQJP0")

    # Overlay our datapoints onto the map
    gmap.heatmap(lats,lons)

    # Generate the heatmap into an HTML file
    gmap.draw("covid19heatmap.html")
    
    
getvirus()
df=pd.read_csv('c:\pythonprograms\Coronavirus\coronadata2.csv')
'''print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)'''
graphcases(df)
datatable(df)
plotmap(df)
#heatmap(df)