#%% Linear Regression -1 Marketing Data - Sales - YT, FB, print


#libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model #1st method
import statsmodels.api as sm  #2nd method
import matplotlib.pyplot as plt
import seaborn as sns

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/R/marketing.csv'
marketing = pd.read_csv(url)
marketing.head()


#%%DESCRIBE DATA
marketing.describe
marketing.shape
marketing.info()
#null values check
marketing.isnull().sum() 

#outlier analysis
marketing.dtypes
fig, axs = plt.subplots(2,2, figsize = (10,5))
plt1 = sns.boxplot(marketing['youtube'], ax = axs[0,0])
plt2 = sns.boxplot(marketing['facebook'], ax = axs[0,1])
plt3 = sns.boxplot(marketing['newspaper'], ax = axs[1,0])
plt4 = sns.boxplot(marketing['sales'], ax = axs[1,1])
plt.tight_layout()
plt.show();


#%%VISUALISE FEW PLOTS TO CHECK CORRELATION

sns.scatterplot(data=marketing, x='youtube', y='sales')
sns.scatterplot(data=marketing, x='facebook', y='sales')
sns.scatterplot(data=marketing, x='newspaper', y='sales')



#%%SPLIT DATA INTO TRAIN AND TEST
from sklearn.model_selection import train_test_split
X= marketing[['youtube', 'facebook', 'newspaper']]
X
y = marketing['sales']
y
X.head()

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.33, random_state=42)
X_train
y_train
X_test
y_test

#%%BUILD THE MODEL
from sklearn.linear_model import LinearRegression
lm = LinearRegression().fit(X_train,y_train)
lm.score(X_train,y_train)  #Adj. R2 
lm.intercept_ # b0 constant
lm.coef_ #b1, b2, b3




#%%PREDICT ON TEST VALUES
predicted_y = lm.predict(X_test)
predicted_y



#%%FIND METRICS - R2, ADJT. R2, RMSE, MAPE
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
mean_squared_error(y_test, predicted_y)
r2_score(y_test, predicted_y)
help(sklearn.metrics)
import math
RMSE = math.sqrt(mean_squared_error(y_test, predicted_y))
RMSE
MAE = mean_absolute_error (y_test, predicted_y)
MAE
import statsmodels.api as sm
X_train_new = sm.add_constant(X_train)
lm_1 = sm.OLS(y_train, X_train_new).fit()
print(lm_1.summary())


#%%PREDICT ON NEW VALUE
newdata = pd.DataFrame({'youtube':[50,60,70], 'facebook':[20, 30, 40], 'newspaper':[70,75,80]})
newdata
pred_newdata = lm.predict(newdata)
pred_newdata
#your ans should be close to [ 9.51, 11.85, 14.18] 


#%%CONCLUSION
print('\nEquation of the model is: \n y = 3.309 + 0.044x1 + 0.19x2 + 0.006x3 \n\nR2 value is 0.910\nAdj. R2 value is 0.907\nMean Squared Error is', mean_squared_error(y_test, predicted_y), '\nRoot Mean Squared Error is',RMSE, '\nMean Absolute Error is', MAE,'\nF-statistic is 435.6\nAIC IS 555.1\nBIC is 566.6')
