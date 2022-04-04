# Group-1-COVID19
## Machine Learning week 1
Much of my time was spent connecting the dataset to the actual google colab spark file.
Setting up the data i used turned out to not have the qualifications to run a mechiene learning software.
My next goal is to connect the whole data set and then use the information to predict covid spikes and their peaks.

## Machine Learning week 2 & 3
Most of this week was spent on analysing the data and to see if it can work with a clustering model. Testing was done on a variety of the columns while non-useful data points were taken out. currently we are using "Infection_Risk", "Case_Fatality_Rate", "Recovery_Proporation", "NewCases", "NewDeaths", "NewRecovered", "ActiveCases" from our data set but these could change depending on the accurecy of your model.

ETL was performed to give us a desired dataset using "country" as an index.

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

We are still gauging to see how to cluster our data and what variables to focus on. We plan to plolish our model and do not need to split the data into a training set as only the values will change and not the tables and columns.
This dataset updates by country and not individually unlike other covid datasets.
Some of the major limitation are we have to use unsupervised lerning so it is hard to gauge accuracy. The benefits are that our question is simple and we can catagorize our data by 5-6 leavels of safety in reguard to certain countries.
Due to the nature of countries and laws it can be tricky to be 100% accurate in reguards to safety but metrics such as "infection rate" and "Death rate" can help us better understand the answer.
