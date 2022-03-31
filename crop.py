import pandas as pd
import datetime

#import csv file and set sep=; since that's what seperates the columns in the csv file
bristol_air = pd.read_csv('bristol-air-quality-data.csv', sep=';')

#print the imported csv to be sure it's imported properly
print(bristol_air)

#select 'Date Time' column and format the datetime 
bristol_air['Date Time'] = pd.to_datetime(bristol_air['Date Time'])

#set the condition for filtering the 'Date Time' column
crop = (bristol_air['Date Time'] >= '2010-01-01')
print(bristol_air.loc[crop])

#write the result of the filter to a csv file, setting the index to False in order not to print any index
bristol_air.loc[crop].to_csv('crop.csv', index=False)

