## Machine Learning Aspect
The primary question we strived to answer was "Is it safe to travel to a certain country?". We decided to use a database that already clusters crucial data points by country. Opting for an unsupervised clustering model, we felt k-mean was a reliable way to categorize data into "safety levels" where each nation will fall into 5 to 6 clusters. Testing was done on a variety of columns and we favoured data points that reflect current events and trends. Data points such as "totalDeaths" and "totalInfection" reflect dated data that could be 2 years old potentially skewing our results. We have decided to use "Infection_Risk", "Case_Fatality_Rate", "Recovery_Proporation", "NewCases", "NewDeaths", "NewRecovered", "ActiveCases", "Serious_Critical" from our data set as it portrays a more current view of the pandemic.

ETL was performed to give us the desired dataset using "country" as an index.

![image1](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/ETL.png)

PCA was performed giving 3 principle component factors.
![image2](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/PC1-3.png)

An elbow graph was then developed allowing us to narrow the numbers of clusters to 5 or 6.
![image3](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/elbow.png)

Clustering was done on multiple different version dates of the data to better guage our accuracy. Both 5 and6 clusters were performed on both.
![image4](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/clustering.png)

Multiple scatter plots were created much like the one below comparing different aspects of the data. We have decided to use Infection_Risk as a y values as it does a good job answering our question "is it safe to travel to a particular country"
![image5](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/scatter.ong.png)

Lastly a 3-d graph was created, we are still testing to see what variables work best.
![image6](https://github.com/mhoussam1/Group-1-COVID19/blob/main/ML_images/3_d.png)

# Conclusion

Creating a clustring dataset was our solution to categorizing countries into "covid-19 danger levels". The dataset we used updates datapoints clustered into countries and not individually unlike other covid datasets which allowed us to better display our results. 
- Some of the major limitations are that we used unsupervised learning so it is hard to gauge accuracy of our model. 
- The benefits of using this clustring model is that is simplifies the results for the user by giving a "danger level" instead of an abetrary list.
- Another benefit is that it reduces error as compared to a ranked list.
- Due to the nature of countries and laws, it can be tricky to be 100% accurate in regards to safety but metrics such as "infection rate" and "Death rate" can help us better understand the answer.

## Recommendation for future analysis
- Comparing this dataset to other data scources is vital in determining the accuracy of our data.
- Comparing our clusting model to other K value models to better determine the accuracy of our model. 
- Incporpating other data scources such as healthcare viability woul;d give us a fuller picutre and create a more accurate clustring system.
