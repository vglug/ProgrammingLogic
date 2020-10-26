#Pandas helps you to managae two-dimension data tables in python.
#Frist import the pandas library.


import pandas as pd
dict = {"dept":["IT","CSE","ECE","MECH"],
         "students":["210","220","230","400"],
         "staff":["5","7","8","14"]}

#Using this DataFrame funcion the data are displayed as table.


Clg_det = pd.DataFrame(dict)
print(Clg_det)

#Another way to create a DataFrame by import csv file using pandas.
#To import the csv file by Using the read_csv() function.

Student_list = pd.read_csv('stu_list.csv')
print(Student_list)

#TO get total number of column and row of the table using shape() function.
 
clg_det.shape

#To get the statistical about the numerical column in a dataset using describe.

clg_det.describe()

#To concatenate the two datasets into one using concat() function.

clg_det = pd.concat([Student_list,Staff_list])
print(clg_det)

