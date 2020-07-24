# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:26:04 2020

@author: Shambo
"""

#%%importing libraries
import pandas as pd


#%%importing csv file
data = pd.read_csv('denco.csv')
data.head()
data.columns

#%% Who are the most loyal Customers?
loyal = data['custname'].value_counts()
print("Top 10 customers by number of transactions:\n \n", loyal.head(10))


#%% Which customers contribute the most to their revenue
#revenuesum is the total revenue per customer
revenuesum = data.groupby(['custname'])['revenue'].sum().reset_index()
revenuesum
#sort revenuesum in descending order
toprev = revenuesum.sort_values(by ='revenue', ascending = 0) 
print("Top 10 customers by total revenue:\n \n", toprev.head(10))


#%%What part numbers bring in significant portion of revenue?
#partrevenue is the total revenue per part number
partrevenue = data.groupby(['partnum'])['revenue'].sum().reset_index()
partrevenue
#sorting partrevenue in descending order
toppart = partrevenue.sort_values(by='revenue', ascending = 0)
print("Top 10 part numbers by total revenue:\n \n", toppart.head(10))


#%%What parts have the highest profit margin?
#partmargin is the total pargin per part number
partmargin = data.groupby(['partnum'])['margin'].sum().reset_index()
partmargin
#sorting partmargin in descending order
topmargin = partmargin.sort_values(by='margin', ascending = 0)
print("Top 10 part numbers by total profit margin:\n \n", topmargin.head(10))


#%%Who are their top buying customers?
print("Top buying customer by number of transactions is:\n \n", loyal.head(1))


#%%Who are the customers who are bringing more revenue?
print("Top customer by total revenue is :\n \n", toprev.head(1))
