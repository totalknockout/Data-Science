# module imports
import mysql.connector as MySQL
import sys
import csv
import datetime

begin_time = datetime.datetime.now()


try:
# set the user and passoword
# connect to MySQL platform
    conn = MySQL.connect(
        user="root",
        password="Kakokako_12345",
        host="127.0.0.1",
        port=3306
    )

    # make and get the cursor
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
    cur.execute("CREATE DATABASE `pollution-db2`") 


    # get a database handle
    cur.execute("USE `pollution-db2`")

    # define the SQL for the tables
    stations_sql = """CREATE TABLE `stations`
                    (`SiteID` int(11) NOT NULL,
                    `Location` text NOT NULL,
                    `geo_point_2d` VARCHAR(45) NULL,
                    PRIMARY KEY(`SiteID`))
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""


    readings_sql = """CREATE TABLE `readings` 
                    (`Reading_Id` int(11) NOT NULL,
                    `Date_Time` DATETIME  NOT NULL,
                    `NOx` FLOAT NULL,
                    `NO2` FLOAT NULL,
                    `NO` FLOAT NULL,
                    `PM10` FLOAT NULL,
                    `NVPM10` FLOAT NULL,
                    `VPM10` FLOAT NULL,
                    `NVPM2.5` FLOAT NULL,
                    `PM2.5` FLOAT NULL,
                    `VPM_2.5` FLOAT NULL,
                    `CO` FLOAT NULL,
                    `O3` FLOAT NULL,
                    `SO2` FLOAT NULL,
                    `Temperature` REAL NULL,
                    `RH` INT NULL,
                    `Air_Pressure` INT NULL,
                    `DateStart` DATETIME NULL,
                    `DateEnd` DATETIME NULL,
                    `Current` TEXT NULL,
                    `Instrument_Type` VARCHAR(32) NULL,
                    `SiteID` int(11),
                    PRIMARY KEY (`Reading_Id`))
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

    schema_sql = """CREATE TABLE `schema`
                    (`Schema_ID` int(3) NOT NULL AUTO_INCREMENT,
                    `Measure` text DEFAULT NULL,
                    `Description` text NOT NULL,
                    `Unit` text NOT NULL,
                    PRIMARY KEY (`Schema_ID`))
                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
                
            
    cur.execute(stations_sql)
    cur.execute(readings_sql)
    cur.execute(schema_sql)
        
    # add the relationships
    cur.execute("ALTER TABLE readings ADD FOREIGN KEY (`SiteID`) REFERENCES stations(`SiteID`);")

    conn.commit()

    # empty list to hold clean.csv
    readings_lines = []

    # empty list to hold schema.csv
    schema_lines = []

    # read schema csv into list
    with open('schema.csv', 'r', encoding='UTF-8') as fp:
        schema_lines = fp.readlines()

    schema_header = schema_lines.pop(0)

    # read in the csv file as a list one at a time
    with open('clean.csv', 'r') as fp:
        readings_lines = fp.readlines()

    readings_header = readings_lines.pop(0)

    #create list to hold rows of repective tables
    schema = []
    stations = set()
    readings = []

    #enumerate through shema_lines list and parse the right rows to new list
    for number, line in enumerate(schema_lines):
        rec = line.split(',')
        schema.append([number+1, rec[0], rec[1], rec[2].strip('\n')])

    #enumerate through readings_lines list and parse the right rows to new list(stations and readings respectively)
    for number, line in enumerate(readings_lines):
        rec = line.split(',')
        stations.add((rec[4], rec[17], rec[18]))
        readings.append([number+1, rec[0], rec[1], rec[2], rec[3], rec[5], rec[6], rec[7], rec[8], rec[9], rec[10], 
                        rec[11], rec[12], rec[13], rec[14], rec[15], rec[16], rec[19], rec[20], rec[21], rec[22], rec[4].strip('\n')])


    # set the autocommit flag to false
    conn.autocommit = False

    # insert data into schema table
    for row in schema:

        #insert schema
        schema_sql = """INSERT INTO `schema` VALUES (%s, %s, %s, %s)"""

        cur.execute(schema_sql, tuple(row))

    # insert data into stations table
    for row in stations:

        #insert stations
        stations_sql = """INSERT INTO `stations` VALUES (%s, %s, %s)"""

        cur.execute(stations_sql, tuple(row))

    # insert data into readings table
    for row in readings:

        #insert schema
        readings_sql = """INSERT IGNORE INTO `readings` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cur.execute(readings_sql, tuple(row))


    conn.commit()
    conn.close()

#catch and report on any error
#exit with 1 (non-error scripts automatically exit with 0)
except BaseException as err:
    print(f"An error occured: {err}")
    sys.exit(1)
