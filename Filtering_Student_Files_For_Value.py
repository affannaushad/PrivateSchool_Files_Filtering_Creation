#Load Required Library
import pandas as pd

#Load The CSV File
df = pd.read_csv('concisedfile.csv')

#Renaming columns to get them prepared for the loop
df = df.rename(columns={'Course': 'Course.0', 'End Date': 'End Date.0'})

#Creating a filtered DataFrame with the Name, OEN, Course, and End Date Column
filtered_df = pd.DataFrame(columns=['Name', 'OEN', 'Course', 'End Date'])

#Creating a loop to sort the huge csv file by rows that contain end date of 2023-11
for i in range(24):  
    a = df[['Name', 'OEN', f'Course.{i}', f'End Date.{i}']] 
    a.drop(0, axis = 0, inplace=True)
    result=(a[a[f'End Date.{i}'] == '2023-11'])
    result = result.rename(columns={f'Course.{i}': 'Course', f'End Date.{i}': 'End Date'})
    filtered_df = filtered_df.append(result, ignore_index=True)

#Sort the result by the course column and make it the index so we can easily group results by courses
filtered_df.sort_values(['Course'], ascending=True,inplace=True)
filtered_df.set_index('Course', inplace=True)
#Additional indexing which can be used to specify a specific course with an end date of 2023-11
filtered_df.loc['ESLEO'].head(50)