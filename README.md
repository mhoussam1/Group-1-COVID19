# Group-1-COVID19
Final project- Group 1 

# Overview of Covid-19 Data Pipeline and Analysis
This project uses  `Python Pandas`  programming language,  Amazon `Kinesis Data Stream`  and `kinesis Firehose`,  AWS `S3` Bucket , AWS `Glue Databrew`, `Tableau` or AWS `Quicksight` services to extract, process/transform and load streaming data from `APIs` into AWS `S3` bucket storage. 
The extracted Covid dataset is used for creating visualization and `ML` algorithms analysis for real time predictions

## Covid-19 Guiding Questions
*1*  What are the trends in the data regarding testing and/or availability by Countries?

*2* What are the overall global trends?

*3* Based on the COVID 19 results, what conclusion can be drawn concerning testing and tests availability?

*4* Is it safe to travel to specific countries, due to covid? 

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
* Extract streaming data from `APIs`, process using `Python Pandas`. 

#### Code Snippet 

 ![Final_code_snippet](https://user-images.githubusercontent.com/92752935/160428643-4fc07fe6-ef69-4948-bbb6-6392cde6818f.png)
 
 (Note: the code didn't work in my notebook but it worked fine in VS code and using command prompt.)
 
#### Command Prompt 

 ![command_prompt_working_python_code](https://user-images.githubusercontent.com/92752935/160423037-936448a6-0660-42ca-aa97-2c28033da7fb.png)

* Write extracted data to `Kinesis data stream` using `command prompt`.

#### Kinesis Datastream
![datastream_monitoring_page1_20220408](https://user-images.githubusercontent.com/92752935/162487638-4d49e8fe-cb8f-4d3c-b237-ef49271ade60.png)
![datastream_monitoring_page2_20220408png](https://user-images.githubusercontent.com/92752935/162487705-97351ce8-4163-4a80-8362-4c20f5a5f288.png)

* 'Kinesis Datastreams' service is used to collect the data records in real-time.

#### Kinesis Delivery Stream 
![deliverystream_monitoring_page1_20220408](https://user-images.githubusercontent.com/92752935/162487790-50c0c7e6-5aa7-4691-a3e2-6a5f470105dc.png)
![deliverystream_monitoring_page2_20220408](https://user-images.githubusercontent.com/92752935/162487837-a3ab1692-b5ed-4b7d-903e-d2ac85fc9faa.png)
 
* `Kinesis firehose` is used as data `stream delivery` for the  the `ETL` process of writing raw data to `landingbucketgroupone-S3 bucket`
 
#### Delivery Stream To S3 Bucket 
 
![landingbucketgroupone_rawdata_stored_20220408](https://user-images.githubusercontent.com/92752935/162487964-30f824b1-480a-4481-92e6-bb244d7a1e84.png)
 
* Parse the data from `landingbucketgroupone-S3 bucket` bucket into `AWS Glues Databrew` for processing.

#### S3 Bucket to AWS Glue Databrew

 ![S3_bucket_to_AWSGlueDatabrew_data](https://user-images.githubusercontent.com/92752935/160427250-1726aa08-0425-4de2-8289-0e419a3bef93.png)
 

* Processed data from `AWS Glues Databrew` is stored in the processed data `S3 bucket` 

#### Processing Job With AWS Glue Databrew

 ![Processed_job_with_AWSGlueDatabrew](https://user-images.githubusercontent.com/92752935/160423983-a3937662-3fcd-486c-9974-22398847af2b.png)

#### Processed Job to S3 Destination 

 ![processed_data_stored_20220408](https://user-images.githubusercontent.com/92752935/162488125-a9d0d32c-dd28-4865-9d89-c55ac8acb5a8.png)

* Data is used for creating visualization and `ML` algorithms analysis for real time predictions. 


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

- In order to keep updated on the status of each of our parts of the project, we message each other regularly through Slack and organize regular zoom meetings.


## Team roles:

- Square: Muhammad Mobied 
- Circle: Charles Obuseh
- Triangle: Iffad Anwar
- X: Rohini Avhad




### Presentation link 23rd March 2022:

https://docs.google.com/presentation/d/1Z9RZ75dkAYALFQxT3V8_-YUyahDBbJdN7xYwa-QtpTg/edit#slide=id.gc6f9e470d_0_0
