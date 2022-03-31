import pandas as pd
import glob
import sys
from datetime import datetime

#import crop.csv generated from task1a
crop = pd.read_csv('crop.csv', sep=',')

#include a try, except statement to prevent the code from crashing.
try: 

    #create a function to hold a dictionary of the station monitors
    def lookup_stations():

        station_monitors = {
            188 : 'AURN Bristol Centre',
            203 : 'Brislington Depot',
            206 : 'Rupert Street',
            209 : 'IKEA M32',
            213 : 'Old Market',
            215 : 'Parson Street School',
            228 : 'Temple Meads Station',
            270 : 'Wells Road',
            271 : 'Trailer Portway P&R',
            375 : 'Newfoundland Road Police Station',
            395 : "Shiner's Garage",
            452 : 'AURN St Pauls',
            447 : 'Bath Road',
            459 : "Cheltenham Road \ Station Road",
            463 : 'Fishponds Road',
            481 : 'CREATE Centre Roof',
            500 : 'Temple Way',
            501 : 'Colston Avenue'
        }

        #create a variable 'lookupStation' to hold the key, value of the station monitors
        lookupStation = {value: key for key, value in station_monitors.items()}
        
        return lookupStation, station_monitors

        
    #create a function to enumerate the crop.csv and satisfy the conditions specified.    
    def filter_records(crop, lookup, station_monitors):

        #create a temporary list to hold the mis-match message we intend to print if the condition is satisfied.
        temp_irr_Index = []

        #use itertuples() to return an iterator yielding a named tuple for each row in the Dataframe
        for rows in crop.itertuples():
            
            #replace null values with '' for both siteID and Location
            if not pd.isna(rows.SiteID) or not pd.isna(rows.Location):

                if str(rows.SiteID) == 'nan':
                    temp_siteID = ''
                else:
                    temp_siteID = int(rows.SiteID)

                if str(rows.Location) == 'nan':
                    temp_location = ''
                else:
                    temp_location = rows.Location 

                #compare rows of the Locations present in the station monitor values (1st condition), if it satisfies 1st condition, execute second condition.
                if rows.Location in station_monitors.values():

                    #now compare the siteID to the Location(remember Location has already been satisfied to match the value pair in the station monitor)
                    if float(rows.SiteID) != float(lookup[rows.Location]):
                        print("SiteID: [{0}] did not match with Location: [{1}] at Line {2}".format(str(temp_siteID),str(temp_location),str(rows[0])))

                        #append mis-match row to already created list
                        temp_irr_Index.append(rows[0])
                    else:
                        pass
                else:
                    print("SiteID: [{0}] did not match with Location: [{1}] at Line {2}".format(str(temp_siteID),str(temp_location),str(rows[0])))

                    #append mis-match row to already created list
                    temp_irr_Index.append(rows[0])
        return temp_irr_Index


    #using OOP we assign our variables and references made in the functions created above
    def main():
        lookup, station_monitors = lookup_stations()

        #store the result of the filter_record() function into a variable
        indexList = filter_records(crop, lookup, station_monitors)

        #drop the result of filter_records() and store in a new variable
        cleanDF = crop.drop(indexList).reset_index(drop=True)
        return cleanDF, indexList

    #import main() to run the initial function and print the lenght of the mis-match
    if __name__ == "__main__":
        result, mismatch = main()
        print("\n{0} lines found in total".format(len(mismatch)))
        file = 'crop.csv'
        remaining_file = glob.glob('crop.csv')

        #write the cleaned data in a file named 'clean.csv' if not a mis-match and print the number of rows returned
        if not remaining_file:
            result.to_csv('clean.csv', sep=',', index=False)
        else:
            result.to_csv('clean.csv', sep=',', index=False, mode='w+')
        print("\n{0} has {1} lines".format('clean.csv',len(result)))

#catch and report on any error
#exit with 1 (non-error scripts automatically exit with 0)
except BaseException as err:
    print(f"An error occured: {err}")
    sys.exit(1)