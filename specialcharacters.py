from importlib.metadata import files

import pandas as pd
import re

#read csv files
data_males = pd.read_csv(r'C:\Users\cecem\Downloads\C_graphics\C_graphics\male_students.csv')
data_females = pd.read_csv(r'C:\Users\cecem\Downloads\C_graphics\C_graphics\female_students.csv')

# Combine the male and female DataFrames for processing
combined_df = pd.concat([data_males, data_females], ignore_index=True)

# Define a regex pattern to identify names containing apostrophes
apostrophe_pattern = re.compile(r"[']")

# Function to check if a name contains an apostrophe
def has_apostrophe(name):
    return bool(apostrophe_pattern.search(name))

# Filter names with apostrophes
specialcharacter_names = combined_df[combined_df['Student Name'].apply(has_apostrophe)]

# Save the filtered names to a new CSV file
specialcharacter_names.to_csv('students_with_special characters.csv', index=False)

