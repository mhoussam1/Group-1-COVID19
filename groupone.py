import boto3
from io import StringIO
from botocore.client import Config
import pandas as pd
import requests
from datetime import datetime
import time
import json
import random
# use kinesis stream
kinesis = boto3.client('kinesis')
stream_name = 'grouponestream'

# set data to write
url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
	"X-RapidAPI-Key": ""
}
response = requests.request("GET", url, headers=headers)
mydata = response.json()
df_json = pd.DataFrame(mydata)
df_json.drop(['TwoLetterSymbol', 'ThreeLetterSymbol'], axis=1, inplace=True)
df_json[['TotalRecovered',"TotalTests",'Population']] = df_json[['TotalRecovered',"TotalTests",'Population']].astype(int)
covid_data = df_json.to_csv(encoding='utf-8', index=False, header=True)
partitionkey = random.randint(10, 100);
response = kinesis.put_record(StreamName=stream_name, Data=covid_data, PartitionKey=str(partitionkey))
print(response)
time.sleep(5)
