# Group-1-COVID19
Final project- Group 1 

# Overview of Covid-19 Data Pipeline and Analysis
This project uses  `Python Pandas`  programming language,  Amazon `Kinesis Data Stream`  and `kinesis Firehose`,  AWS `S3` Bucket , AWS `Glue Databrew`, `Tableau` or AWS `Quicksight` services to extract, process/transform and load streaming data from `APIs` into AWS `S3` bucket storage. 
The extracted Covid dataset is used for creating visualization and `ML` algorithms analysis of for real time predictions

## Covid-19 Guiding Questions
*1*  What are the trends in the data regarding testing and/or availability by Countries?

*2* What are the overall global trends?

*3*  Based on the COVID 19 results, what conclusion can be drawn concerning testing and tests availability?

*4*   Is it safe to travel to specific countries, due to covid? 

#### Null hypothesis: 
* All countries are equal when it comes to traveling. 

#### Focus areas:
* New confirmed cases
* New deaths
* New recovered
* Total confirmed
* Total death
* Total recovered


## Process Overview 
* Extract streaming data from `APIs`, process using `Python Pandas` 

#### Code Snippet 

 ![code_snippet.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/code_snippet.png) 
 
* Write extracted data to `Kinesis data stream` using `command prompt`

#### Command Prompt 

 ![command_prompt.PNG](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/command_prompt.PNG) 

#### Kinesis Datastream

 ![kinesis-datastream.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/kinesis-datastream.png) 
 
* `Kinesis firehose` is used as data `stream delivery` for the  the `ETL` process of writing raw data to `AWS landing data S3 bucket`

#### Kinesis Delivery Stream 

 ![kinesis-deliverystream.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/kinesis-deliverystream.png) 
 
#### Delivery Stream To S3 Bucket 
 
 ![kinesistos3.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/kinesistos3.png) 
  
* Parse the data from `S3 landing` bucket into `AWS Glues Databrew` for processing

#### S3 Bucket to AWS Blue Databrew

 ![s3dataindatabrew.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/s3dataindatabrew.png) 
 

* Processed data from `AWS Glues Databrew` is stored in the processed data `S3 bucket` 

#### Processing Job With AWS Glue Databrew

 ![databrewprocesstos3.PNG](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/databrewprocesstos3.PNG) 

#### Processed Job to S3 Destination 

 ![processeddatafromdatabrewtos3.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/processeddatafromdatabrewtos3.png)
 
* Data is used for creating visualization and `ML` algorithms analysis of for real time predictions 


#### Sample Dataset
 
 ![sampleprocesseddata.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/sampleprocesseddata.png)   


#### Data Streaming Architecture

![Picture1.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/Picture1.png)
---
## Business Impact of building data pipelines
* Saves time and effort for BI analysts
* Manual process of cleaning, validating of raw data takes on an average of 3-4 hours of time for each and every raw file received at a certain interval of time.
* Automating this simple process saves 3-4 hours for each run and saves effort and time for Data engineers as well as Analysts
* Only pipeline monitoring and maintenance needs to be taken care of once the pipeline is built.
* Grabbing the data from source `APIs`to destination systems AWS `S3` bucket for real time streaming data


## Communication Protocols

- In order to keep updated on the status of each of our parts of the project, we message each other regularly through Slack and organized regular zoom meetings.


## Team roles:

- Square: Muhammad Mobied 
- Circle: Charles Obuseh
- Triangle: Iffad Anwar
- X: Rohini Avhad


### Presentation link:

https://docs.google.com/presentation/d/1Z9RZ75dkAYALFQxT3V8_-YUyahDBbJdN7xYwa-QtpTg/edit#slide=id.gc6f9e470d_0_0


### Link to Tableau Story


