**Technology used** : Python

**Database** : mongoDB

**Data Model** : Key-Value



Some of the limitations of RDBMS technology resulted to the invention of NoSQL databases.
NoSQL databases give better performance than RDBMS.
They are more flexiblle.

**Advantages Of Using NoSQL DataBases**

Each form of NoSQL database has its own set of advantages, however, they all have the same basic capabilities:


1. A scale-out architecture can handle massive amounts of data at rapid speeds.

1. Allow for quick adjustments to schemas and fields.

1. Storing unstructured, semi-structured, or structured data.

1. Make it easy for developers.

1. Use the cloud to its maximum potential to ensure no downtime. 

**Replicating TASK 4B to NoSQL data model,**

1. Imported &#39;clean.csv&#39; file from the &#39;bristol-air-quality-data.csv&#39; from Task 1B as a DataFrame.
1. Proceed to converted the structure to a Key-Value Pair (Key-Value is the structure of a python Dictionary).
1. Renaming the keys (pm2.5, vpm2.5) is vital because they are having a Full points and NoSQL database does not accept full point in the key. 

**Setting up NoSQL database,**

1. I had issues installing MongoDB on my machine, so I went ahead to use their cloud service. I created a Cluster in MongoDB Atlas online;
1. I then went ahead to create a Database &quot;bristol-air-quality-db&quot;
1. Haven done this, a collection was created &quot;bristol-air-quality-doc&quot; under the database &quot;bristol-air-quality-db&quot;
1. Ran the Cluster Network with the above setup producing the link to connect.

**Connecting Python and NoSQL database and Populating data into the Data Base,**

1. The first step was to install and imported module pymongo
1. Using the service MongoClient from the module pymongo I connected to the collection through the cluster network.
    ```python 
    user = MongoClient("mongodb+srv://admin:pass123@cluster0.7lls9.mongodb.net 
    /bristol-air-quality-db?retryWrites=true&w=majority", ssl=True,ssl_cert_reqs='CERT_NONE')
    ```

1. After a successful connection, using the object created, I connected to database &#39;bristol-air-quality-db&#39; and connected to the respective collection &#39;bristol-air-quality-doc&#39; under the database.

    ```python
    db = client['bristol-air-quality-db'] 
    collection = db['bristol-air-quality-doc']
    ```

1. Using the function insert\_many from the collection, I populated the list of key-value(mongoDB default view) data to the database collection.

    ```python
    collection.insert_many(keyValueData);
    ```

**Recreating Query in MongoDB**

1. Aggregate data processing pipeline methodology was used here.
1. In the first pipeline, custom field operators was constructed; minutes and years, because the query involves the time in minute and year. This would make it easy to query in the subsequent pipeline.
1. Next pipeline, matching with year 2019 and minutes equal to 60\*8 (60 hours \* 8 = 8AM).
1. In the final pipline, grouping with average of particulate matter <2.5 micron diameter (pm2.5), average of volatile particulate matter <2.5 micron diameter (vpm2.5) by each siteID (site_id) matching the previous pipeline conditions (2019 at 8AM).
1. Verified the results.

**Script for populating data to the database**

```python
# Importing Library 
import pymongo 
from pymongo import MongoClient 
import pandas as pd 
from datetime import datetime, tzinfo, timezone 
 
# Import csv file and convert to JSON 
fileName = 'bristol-air-quality-data.csv' 
inputData = pd.read_csv(fileName, sep=",", low_memory=False) 
  
# Converting DataFrame to list of dictionaries 
dictData = inputData.to_dict("records") 
  
# Replacing columns having underscores with full points  
for eachDict in dictData: 
    eachDict['pm2_5'] = eachDict.pop('pm2.5') 
    eachDict['vpm2_5'] = eachDict.pop('vpm2.5') 
     
# Connecting to MongoDB  
client = MongoClient("mongodb+srv://admin:pass123@cluster0.7lls9.mongodb.net/bristol-air-quality- db?retryWrites=true&w=majority", ssl=True,ssl_cert_reqs='CERT_NONE') 
 
# Importing Database 
db = client['bristol-air-quality-db'] 
# Importing Collection 
collection = db['bristol-air-quality-doc'] 
  
# Populating Values to the collection 
collection.insert_many(dictData) 
```

**Query in MongoDB -  Return the mean values of PM2.5 (particulate matter <2.5 micron diameter) & VPM2.5 (volatile particulate matter <2.5 micron diameter)** **by each station for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity)**

```mongodb
bristol-air-quality-doc.aggregate[ 
    { 
        '$addFields': { 
            'minutes': { 
                '$sum': [ 
                    { 
                        '$min': '$date_time' 
                    }                     
                    { 
                        '$multiply': [ 
                            { 
                                '$hour': '$date_time' 
                            }, 60 
                        ] 
                    } 
                ] 
            }, 
            yrs: { 
                '$sum': [ 
                    { 
                        '$year: '$date_time' 
                    }              
                   ] 
            } 
 
        } 
    }, { 
        '$match': { 
            '$and': [ 
                { 
                    'yrs':  
                    { 
                        '$eql': 2019 
                    } 
                },  
                { 
                    'mins':  
                    { 
                        '$eql': 60 * 8 
                    } 
                }, 
            ] 
        } 
    },  
    { 
        '$group': { 
                  'site_id':'$siteid',  
                  'avg_pm2.5': {'$avg':"$pm2.5"}, 
                  'avg_vpm2.5': {'$avg':"$vpm2.5"}  
                  }  
    } 
]); 
```

**Output**
```
[
  {
    "_id": 607da86bebd533ade4ea809f
    "site_id": 203,
    "avg_pm2_5": 0.000,
    "avg_vpm2_5": 0.000
  },
  {
    "_id": 607da86bebd533ade4ea8081
    "site_id": 215,
    "avg_pm2_5": 1.79632,
    "avg_vpm2_5": 0.00000
  },
  {
    "_id": 607da86bebd533ade4ea8057
    "site_id": 270,
    "avg_pm2_5": 0.00000,
    "avg_vpm2_5": 0.00000
  },
  {
    "_id":607da86bebd533ade4ea80e7
    "site_id": 452,
    "avg_pm2_5": 9.25227,
    "avg_vpm2_5": 0.00000
  },
  {
    "_id": 607da86bebd533ade4ea8d62
    "site_id": 463,
    "avg_pm2_5": 0.00000,
    "avg_vpm2_5": 0.00000
  },
  {
    "_id": 607da86bebd533ade4ea815f
    "site_id": 500,
    "avg_pm2_5": 0.00000,
    "avg_vpm2_5": 0.00000
  },
  {
    "_id": 607da86bebd533ade4ea8520
    "site_id": 501,
    "avg_pm2_5": 0.00000,
    "avg_vpm2_5": 0.00000
  }
]
```

