#Topic: Outlier Analysis
#-----------------------------
#why analyse - The presence of outliers in a classification or regression dataset can result in a poor fit and lower predictive modeling performance.
#an outlier is an observation point that is distant from other observations.
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#sample data
marks1 = [3,50,74,76,81,54,85,67,77,41]
len(marks1)

import seaborn as sns
sns.boxplot(x=marks1)
plt.show();

marks2 = [61,45,66,57,64,56,77,64,67,11]

sns.boxplot(x=marks2)
plt.show();

#Method 1 - graphically
plt.scatter(x=marks1, y=marks2)
plt.show();


#Method 2 - z score
from scipy import stats

z = np.abs(stats.zscore(marks1))
print(z)

#finding outlier using z-score
#https://statisticsbyjim.com/basics/outliers/#:~:text=Using%20Z%2Dscores%20to%20Detect,mean%20that%20each%20value%20falls.&text=A%20standard%20cut%2Doff%20value,3%20or%20further%20from%20zero.
np.where(z > 3)
np.where(z > 2)


#Method 3 - quantile method
Q1 = pd.Series(marks1).quantile(0.25)
Q3 = pd.Series(marks1).quantile(0.75)
Q1, Q3
IQR = Q3 - Q1
IQR
IQR2 = stats.iqr(pd.Series(marks1)) 
IQR2

#outlier : < Q1 - 1.5*IQR or > Q3 + 1.5*IQR
(marks1 < Q1-1.5*IQR) | (marks1 > Q3+1.5*IQR)

#dataframe
from pydataset import data
data('Boston') #https://www.engineeringbigdata.com/boston-dataset-scikit-learn-machine-learning-in-python/#:~:text=The%20sklearn%20Boston%20dataset%20is,and%20descriptions%20of%20each%20column.
boston = data('Boston')

boston.head()
boston.columns
#box plot
sns.boxplot(x=boston['dis'])
# plot shows three points between 10 to 12, these are outliers as there are not included in the box of other observation i.e no where near the quartiles.

#scatterplot
boston.columns
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(boston['indus'], boston['tax'])
ax.set_xlabel('Proportion of non-retail business acres per town')
ax.set_ylabel('Full-value property-tax rate per $10,000')
plt.show();
#most of data points are lying bottom left side but there are points which are far from the population like top right corner.

#Z-score
z = np.abs(stats.zscore(boston))
print(z)
#difficult to say which data point is an outlier. Let’s try and define a threshold to identify an outlier.
threshold = 3
print(np.where(z > threshold))
#confused by the results. The first array contains the list of row numbers and second array respective column numbers, which mean z[55][1] have a Z-score higher than 3
print(z[55][1])

#IQR
Q1 = boston.quantile(0.25)
Q3 = boston.quantile(0.75)
IQR = Q3 - Q1
print(IQR) # of each column
#The below code will give an output with some true and false values. The data point where we have False that means these values are valid whereas True indicates presence of an outlier.
print((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR)))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR)))
dfTF = (boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR))

sns.boxplot(x=boston.crim)

dfTF.sum(axis=0)
dfTF.crim.value_counts()


#Z-score
#want to remove or filter the outliers and get the clean data. This can be done with just one line code as we have already calculated the Z-score.
dfTF[(z<2).all(axis=1)]
boston_wo = boston[(z < 3).all(axis=1)]
boston_wo.head()

boston.shape
boston_wo.shape

boston_wo2 = boston[~((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR))).any(axis=1)]
boston_wo2.shape

sns.boxplot(x=boston_wo2.zn)


#https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
#https://haridas.in/outlier-removal-clustering.html