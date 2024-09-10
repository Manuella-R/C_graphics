from importlib.metadata import files

import pandas as pd

#read excel files
data_males = pd.read_csv(r'C:\Users\cecem\Downloads\C_graphics\C_graphics\male_students.csv')
data_females = pd.read_csv(r'C:\Users\cecem\Downloads\C_graphics\C_graphics\female_students.csv')

#save as CSV files
data_males.to_csv('students_male.csv', index=False)
data_females.to_csv('students_female.csv', index=False)

#save as TSV files
data_males.to_csv('students_male.tsv', sep='\t', index=False)
data_females.to_csv('students_female.tsv', sep='\t', index=False)

