#!/usr/bin/env python
# coding: utf-8

# ##### Coded By Harshanthi

# Reference:
# https://medium.com/analytics-vidhya/how-to-extract-information-from-your-excel-sheet-using-python-5f4f518aec49
# 
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# 
# https://www.dataquest.io/blog/excel-and-pandas/
# 
# https://github.com/pandas-dev/pandas/issues/10559

# In[1]:


#Make sure the Excel you will be working with is in your current working directory
import os 
os.getcwd()
#this changes our CWD, if the excel sheet is not in CWD
#os.chdir('C:\\Users\\harsh\\Ismile Technologies\\Restaurant Management') 

#work on excel sheet
import openpyxl
import xlrd

import pandas as pd


file = 'donation.xls'
data = pd.read_excel(file)


# #gives all the sheet names in the workbook
# print(data.sheet_names)

# #working with dishesList
# df = data.parse('dishesList')
# 


data.info

data.head(10)


#integrate location based indexing
#data.iloc[0:] 



#reading each sheet1 from the excel, i.e, dishesList
dishesList = pd.read_excel(file, sheet_name=0, index_col=0)
dishesList.head()   


#exploring the data
dishesList.shape



#set_index is menu items ...retrieves the quantity left in grams
#dishNames = dishesList.iloc[:,-1]
#print(dishNames)



#Gives all the dishes who's quantity is above 1000 grams
donationItems = dishesList.loc[dishesList['Quantity(grams) Dishes left at( 8:00 PM )'] >= 1000,'Quantity(grams) Dishes left at( 8:00 PM )']
print(donationItems)



#reading each sheet2 from the excel, i.e, email details(mycontacts)
mycontacts = pd.read_excel(file, sheet_name=1, index_col=0)
mycontacts.head()


#reading each sheet3 from the excel, i.e, email body message
messages = pd.read_excel(file, sheet_name=2, index_col=0)
messages.head()



# %%