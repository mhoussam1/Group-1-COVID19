# Group-1-COVID19
Final project- Group 1 
# Group-1-COVID19
Final project- Group 1 

# Overview of Covid-19 Data Pipeline
This project uses `SQL`, `Python3`, `Pyspark` programming languages and Amazon Managed Workflows for Apache Airflow `(MWAA)`, AWS `S3`, AWS `Athena`, `Tableau` or AWS `Quicksight` services to;

* Extract, process/transform and load streaming data from `APIs` into AWS `S3` bucket storage.

#### Code Snippet

 ![code_snippet.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/code_snippet.png)

* The process of extraction to saving data is orchestrated using Amazon Managed Workflows for Apache Airflow `(MWAA)` 
* Data query is achieved using  AWS `Athena`
* Data is used for creating visualization and `ML` algorithms analysis of for real time predictions 

## Covid-19 Guiding Questions
*1* What are the trends in the data regarding testing and/or availability by Countries? 

*2* What are the overall global trends? 

*3* Based on the COVID 19 results, what conclusion can be drawn concerning testing and tests availability?

#### Focus areas:
* New confirmed cases
* New deaths
* New recovered
* Total confirmed
* Total death
* Total recovered

#### Sample Dataset
 
 ![sampledataset.png](https://github.com/mhoussam1/Group-1-COVID19/blob/charleside2001/images/sampledataset.png)   


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
