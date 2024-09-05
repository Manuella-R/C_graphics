import pandas as pd
import logging

# Libraries imported to load and process data from excel and to set up logs to files
# Load the data from an excel sheet
df = pd.read_excel(r'C:\Users\rehem\Downloads\TestFiles.xlsx')  

# Setup logging
logging.basicConfig(filename='student_logs.log', level=logging.INFO)

# Separate lists of male and female students and filter them
male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

# Log the counts and return the row numbers in each file
logging.info(f"Number of Male Students: {len(male_students)}")
logging.info(f"Number of Female Students: {len(female_students)}")

# Save the separated lists and export the dataframes in csv files
male_students.to_csv('C_graphics/male_students.csv', index=False)
female_students.to_csv('C_graphics/female_students.csv', index=False)
