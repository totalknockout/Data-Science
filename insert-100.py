import csv
import itertools
from datetime import datetime
import sys

#create an empty list to hold the insert-100 readings
count = 1
readings = []


sql = "INSERT INTO readings VALUES \n"

#Use itertools to iterate through the first 100 rows
with open('clean.csv') as csvfile:
    for row in itertools.islice(csv.DictReader(csvfile, delimiter = ","), 100): 

        #delete location and geo_point_2d
        del row['Location']
        del row['geo_point_2d']

        # Format all Date and Time format to the ISO standard format
        date_time = datetime.fromisoformat(row['Date Time'][:-6])
        date_time.strftime('%Y-%m-%d %H:%M:%S')
        row['Date Time'] = date_time

        date_start = datetime.fromisoformat(row['DateStart'][:-6])
        date_start.strftime('%Y-%m-%d %H:%M:%S')
        row['DateStart'] = date_start

        if row ['DateEnd']:
            date_end = datetime.fromisoformat(row['DateEnd'][:-6])
            date_end.strftime('%Y-%m-%d %H:%M:%S')
            row['DateEnd'] = date_end

        #convert eaxh value to a string
        readings = ["'" + str(x) + "'" for x in row.values()]

        #use join to add values to reading list
        readings = ",".join(readings)

        #Replace empty values with NULL, and convert the boolean True and False to strings 'True' and 'False'
        readings = readings.replace("''", " NULL")
        readings = readings.replace("'True'", " True")
        readings = readings.replace("'False'", " False")

        sql += '(' + str(count) + ', ' + readings + '),' + '\n'

        count += 1


new_sql = sql[:-2]
file = open("insert-100.sql", "w")
file.write(new_sql + "\n")
print(new_sql)

