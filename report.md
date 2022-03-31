## **REFLECTIVE REPORT ON THE DATA MANAGEMENT FUNDAMEMTALS ASSIGNMENT**

---

At the initial stages of the term when the module leader mentioned the assignment, I must admit I was anxious and at the same time excited about the learning process. Through this process, I have been able to improve my python programming skills, learnt how to design an efficient ER model, to create and populate a DataBase automatically using SQL in python, running simple queries on my DataBase and NoSQL data modelling. Ultimately, the whole process is a roadmap to what Data Management Fundamentals entails.

When the assignment was published, the module leader explained the whole purpose of the assignment and also walked us through each tasks, expectations and assessment criteria. I also went ahead to read about the data provided to understand the problem and the reason behind why the data was gathered via the link - [UK Government Air Quality Strategy](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/69336/pb12654-air-quality-strategy-vol1-070712.pdf), which was helpful to understanding possible visualisations that can be done to understand and analyse the data. 

**Some possible Visualisation that can be done on the data are:**

* Scatterplot : to find relationship between two variables. 
* Heatmap: to find multi-collinearity. 
* Distplot: to show distribution. To name a few. 

All of these plots can be done using python's data visualisation libraries like matplotlib, seaborn and plotly. 



### ***Problem Solving approach to the tasks***


**Task 1A:**

For this task, I imported two libraries pandas and datetime to help crop the &#39;bristol-air-quality-data.csv&#39; data. 
Here are the steps I followed:

1. I imported the &#39;bristol-air-quality-data.csv&#39; into my working environment.

1. I then went ahead to format my &#39;Date Time&#39; column to allow for easy filtering.

1. I then set my condition for filtering the &#39;Date Time&#39; column, which is deleting any record before 00:00 1 Jan 2010.

1. And then I wrote the result into a csv file named &#39;crop.csv&#39;.


**Task1B:**

For this task, I imported four libraries pandas, glob, sys and datetime to help clean the &#39;crop.csv&#39; file generated from task1b. 
Here are the steps I followed:

1. I first imported the &#39;crop.csv&#39; with the help of pandas. 

1. I then included a try except statement to help me handle error. 

1. I created my first function to hold a dictionary of the station monitors and assigned the key, value pair to a lookupstation. 

1. I created a temporary list to hold the mismatch and then replaced null values with ' '. 

1. I then went ahead to create series of functions to satisfy the condition of the task which is to remove any dud record or mismatch. 

    * The first function checks if the Locations from the DataFrame matches with the station monitor values.

        * When the first condition is satisfied, the second statemnt compares the siteID with the Location from the lookup to see if it matches. If it doesn't match it prints a message and stores the mis-match row to the already created list. 

    * The second function takes the result from the first function, drops the rows which are mis-match that was stored in the temporary list from the data and prints the number of mismatch. If not a mismatch, it writes the rows to a new csv file named &#39;clean.csv&#39; and prints the number of rows written. 


**TASK 2A:**

In this task, I studied the data given, identified the primary keys and broke the table into three parts (stations, readings and schema) with schema acting as guide and description of the data. I then went ahead to create a relationship between them. This task was done on MySQL workbench. 


**TASK 2B:**

In this task, I used the MySQL forward engineer to create an SQL schema with my ER model from task 2a.

**TASK 3A:**

1. I first import a few libraries namely MySQL connector, sys, csv, datetime and then connection to MySQL server from my python environment. 

1. I then created a database and the three tables with all the entities and their data-types.

1. After that, two lists were created to hold the clean.csv and schema.csv.

1. I later went ahead to create 3 separate lists, and then enumerated through the two csv's and parsed the right rows into their respective lists. 

1. Insert data from the 3 seperate lists into the respective table created in the database and close connection.

**TASK 3B:**

For this task, a list was created to hold the insert-100 readings. And then using itertools iterate through the first 100 rows and write the result to an sql file. 

**TASK 4A,B,C:**

Simple SQL queries were run on the database created.

**TASK 5:**

For this task I selected MongoDB which is a very popular NoSQL database and has so many resources. I did my research and discovered some of the advantages of NoSQL over RDMS. I then went ahead to replicate one of the SQL queries from task 4 in this task. 





