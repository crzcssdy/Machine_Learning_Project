# Project 4: Machine Learning and Predicting Obesity

# Overview
Obesity has been a rising health concern among most modern populations for the last few decades. There are numerous health risks, both  immediate and long-term, that can have detrimental consequences to the longevity and quality of life for an individual. Such consequential impacts include but are not limited to: respiratory difficulties, increased risk of fractures, hypertension, diseases of the gallbladder and pancreas, increased mental health issues, increased risk of non-communicable diseases, and more. As such, it is important for policymakers and the general public to understand not just the impact of obesity, but the leading causes that contribute significantly to obesity rates. Our goal for this project is to further understand and visualize the leading contributors to growing obesity rates in populations such as Colombia, Peru and Mexico, and develop a machine learning model that can support health initiatives to manage overweight and obesity by predicting obesity levels based on lifestyle parameters.  The classification model must have decent level of accuracy (> 75%), interpretability of feature importance, and flexibility/resistance ot overfitting in order to be effective.

## Data Source, ETL, and Database Creation
For our analysis, we primarily used the dataset gathered and compiled by Fabio Mendoza Palechor and Alexis de la Hoz Manotas with the technical assistance provided by the Universidad de la Costa (CUC). The dataset was used in relation to Palechor and Manotas' academic article "Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico", published in August 2019. We chose this dataset specifically because the information gathered correlates strongly with the data needed to develop our machine learning model for predicting obesity. 

Furthermore, this paper contains data regarding eating habits and physical conditions of individuals ages 14 and 61, using a web platform with a survey where anonymous users answered each question, to which the information was processed obtaining 17 attributes and 2111 records, after utilizing a balancing process known as SMOTE. The attributes identified with eating habits are: Frequent consumption of high caloric food (FAVC), Frequency of consumption of vegetables (FCVC), Number of main meals (NCP), Consumption of food between meals (CAEC), Consumption of water daily (CH20), and Consumption of alcohol (CALC). The attributes related with the physical condition are: Calories consumption monitoring (SCC), Physical activity frequency (FAF), Time using technology devices (TUE), Transportation used (MTRANS), other variables obtained were: Gender, Age, Height and Weight.  Each record also includes a respondent's obesity level classification which is assigned based upon their body mass index (BMI), derived from the their height and weight.

Link to the article can be found here: https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub

Link to the raw dataset can be found here: https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition

The raw dataset was then cleaned and refined (confirming the non-existence of null values, data type as needed based on the field, naming conventions changed to be more intuitive, etc.) and uploaded into a PostgreSQL database.  The decision to use a PostgreSQL database was largely due to its ease of use and the ability to quickly implement it locally without extensive use of resources.  The files associated with this ETL phase of the project are available in the 'ETL' folder and include the following:
* ETL_ObesityDataSet.ipynb - used to clean and refine the raw dataset
* obesity_db_ERD.png - an ERD of the final PostgreSQL database
* obesity_db_PostgreSQL_table_schemata.sql - PostgreSQL code for the database/table creation
* Resources - folder containining the raw dataset and the cleaned dataset in .csv format

## Model Choice and Dependencies
After cleaning the data, an exploratory data analysis was conducted to determine the features of our potential model (work contained in the files 'EDA_Obesity_Dataset.ipynb' and 'Additional EDA and Potential Model Comparison.ipynb').  Our EDA revealed that correlations/relationships existed between almost all the fields within the dataset and were viable features to be used in our classification model.  However, height and weight were excluded from the feature set due to their direct relationshipo to BMI/Obesity classification.
Once the features were determined, the dataset separated out into training and test sets and fitted to three different models: Decision Tree, Gradient Boosting, and Random Forest.  Based on the criteria of accuracy, interpretability, and flexiblity, the Random Forest model was the best performing of the three and became the model of choice (analysis and model comparison conducted in file 'Additional EDA and Potential Model Comparison.ipynb')

## Initial Results and Optimization Efforts
The inital Random Forest classification model had an 84.87% accuracy rate with an average cross validation accuracy of 85.19%.  While this met all of the model requirements we had initially laid out, we still sought to improve the accuracy through optimization (conducted in file 'Obesity_Classification_Model_Setup_&_Optimization.ipynb').  Our first attempts sought to improve the model via feature engineering.  Given the complexities of the data collection and the inclusion of synthetic samples within the dataset, we opted to not try to incorporate additional data from other sources as that would increase the complexity and likely be detrimental to our efforts.  Instead we focused potentially removing 'noise' from the model that could be caused by features with little influence on the predictive model as per its Gini importance.
![alt text](<<Images/Feature Importance_Initial.png.png>)

The first two optimization attempts tried to apply this appraoch by removing the lowest two and then the lowest three features based on Gini importance.  However, this approach resulted in subsequent decreases in both accuracy and average CV accuracy with each revision.

![alt text](<Images/Accuracy Comparison _Initial_1_2.png>)![alt text](<Images/CV_Accuracy Comparison _Initial_1_2.png>)

Our third attempt at optimization focused on tuning the model's hyperparameters, specially using scikit-learn's RandomSearchCV function to determine the best performing set of parameters.  This approach resulted in an increase accuracy to 87.00% and average CV accuracy to 86.55%.  This third and final optimization attempt would be our final model.

![alt text](<Images/Accuracy Comparison _Initial_3.png>)![alt text](<Images/CV_Accuracy Comparison _Initial_3.png>)
## Final Model Summary
Our final Obesity classifcation model is a Random Forest Classifier with an overall accuracy of 87.00% and an average of CV accuracy of 86.55%.  These figures demonstrate the model's predictive power as well as its  flexibility to new data respectively.  When looking at the classification report we see that the model also does a good job at predicting each Obesity level with the weakest performing classification being Normal Weight.

![alt text](<Images/Classification Report_Final.png>)

Looking at the confusion matrix, we see that the model tends to slightly overestimate the obesity level of actual Normal Weight instances.  Given the objective of the model to be a guide/tool to help manage the prevalence of obesity, we decided that this slight overestimation of higher obesity levels in actual Normal Weight instances was acceptable.

![alt text](<Images/Confusion Matrix_Final.png>)
## Conclusion
The objective of this project was to develop a machine learning model that could predict levels of obesity based on a series of lifestyle factors.  Based upon the results of our final model, we can say that we sucessfully acheived this and met our requirements of prediction accuracy, intepretability of features, and flexibility to new data.  Some potential applications of this model could be the prediction of underlying health conditions for individuals or groups whose BMI/Obesity level conflict with the model's classification or the use of the model's feature importance to inform policy makers and health care providers on the factors that most influence obesity.

# Technologies Used & Dependencies
* Python via jupyter notebook
* PostgreSQL Database
* Scikit-Learn
* Pandas
* Numpy
* Seaborn
* Matplotlib

# Installing & Execution
The repository files can be downloaded to open and execute the jupyter notebook files:
* EDA_Obesity_Dataset.ipynb
* Additional EDA and Potential Model Comparison.ipynb
* Obesity_Classification_Model_Setup_&_Optimization.ipynb

Note that since the files contain relative file paths, it is important that the file locations within the SurfsUp directory are not changed in order for the files to execute properly.

# Ethical Considerations
In developing this data visualization project, we were committed to upholding the highest ethical standards. We prioritized transparency by using publically available datasets as noted form the published dataset, clearly documenting our methodologies, and any assumptions made during analysis. We recognize the potential impact of our work and remain dedicated to promoting responsible data usage, fostering trust, and encouraging informed decision-making.  We were also mindful of any potential biases that could have been introduced choosing metrics and comparing data for various countries.  We endeavored to conduct additional research and review in order to maintain as much objectivity and representation as possible.

# Authors
Assiba Lea Apovo, Cassidy Cruz, Widchy Joachim, Daniel Pineda, and Edward Tabije

# Acknowledgments
Machine_Learning_Project was created as an assignment for the University of California, Irvine Data Analytics Bootcamp - June 2024 Cohort under the instruction and guidance of Melissa Ingle (Instructor) and Mitchell Stone (TA). The practical exercises and coding examples demonstrated through the bootcamp helped inform and inspire the code for this project.
