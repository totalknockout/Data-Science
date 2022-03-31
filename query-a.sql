#Return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) found in the dataset for the year 2019.

SELECT Date_Time as `Date Time`, max(NOx) as `Highest Value Of Nitrogen Oxide`, Location as `Station Name` FROM stations, readings WHERE year(Date_Time) = '2019' GROUP BY Date_Time, Location DESC LIMIT 1;