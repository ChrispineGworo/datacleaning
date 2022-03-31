import numpy as np
import pandas as pd
from pandas import DataFrame

data=DataFrame({'Date':['2/1/2022','3/1/2022','4/1/2022','6/1/2022','7/1/2022','9/1/2022','10/1/2022','11/1/2022','14/1/2022','17/1/2022','18/1/2022','20/1/2022','23/1/2022','25/1/2022','26/1/2022','28/1/2022','29/1/2022','2/2/2022','3/2/2022','5/2/2022','6/2/2022','7/2/2022','9/2/2022','10/2/2022','11/2/2022','13/2/2022','15/2/2022','16/2/2022','18/2/2022','20/2/2022'],'City':['London','London','London','London','London','Singapore','Singapore','Singapore','Sydney','Sydney','Sydney','Sydney','Sydney','Sydney','Toronto','Toronto','Toronto','Toronto','New York','New York','New York','Dubai','Dubai','Dubai','Dubai','Doha','Doha','Doha','Doha','Doha'],'Population':[6782,7657,8466,9467,67567,4987,7856,87757,46889,96546,6678,4356,7789,6456,86678,8664,4667,7557,8567,4467,9766,65467,7557,4678,8666,56788,6678,75454,9766,5678],'Revenue':[3876,86678,77556,86556,75677,75678,8588,65746,96678,5685,9746,8567,5677,7567,6888,5667,7678,9678,45678,6534,97667,8555,46776,6436,95468,64366,9766,74478,75346,86468],'Cost':[446,976,678,576,888,955,177,877,665,992,5877,5567,8658,8657,8758,3446,7666,9778,7576,4567,8767,9667,756,768,567,876,8658,665,7557,5678],'Percentage':[53.7,68.9,34,33,23,65.4,56,76.87,77,85,90,63.9,65,67,53.5,76,87,38.2,76,98,77.86,67,98,76,87,66.5,67.87,35.45,54.7,67.834],'Promo':["medium","high","high","medium","low","low","high","medium","medium","high","low","high","low","high","high","medium","high","medium","low","low","high","high","medium","high","low","low","low","medium","high","high"]})

print(data.columns.str.upper())
print("")
print(data.rename(columns={'City':'Cities'}))
print("")
print(data.isnull().any())
print("")
#general comment on whether there is any missing value anywhere in the dataframe
print(data.isnull().any().any())
print("")
#total of missing values per column
print(data.isnull().sum())
print("")
#the total of missing values
print(data.isnull().sum().sum())
print("")
#replacing any missing value with 0
print(data.fillna(0))
print("")
#dropping missing values and knowing the final shape of the entire data
print(data.dropna().shape)
print("")
#how to drop columns with missing values
print(data.dropna(how="any").head())#you can also use (thresh=2(more than 2)) or (axis=1)
print("")
