# Email generator using pandas

## An introduction to using pandas for data processing of excel files

This project demonstrates how to use pandas in Python . It includes examples of how to manipulate student data to:

1. generate student emails given their names
2. count the number of male and female students
3. logging the outputs

## Features

- Email generation
- Gender count
- Logging

## Prerequisites

- Python 3 and above
- pandas library (for data processing)
- openpyxl library(for handling excel files)
- logging (already installed with python)
  pandas and openpyxl can be installed from command line using the command
  **pip install pandas openpyxl**

## How it works

**Email generator**
The program reads the student names from an excel file and generates an email address for each student. It works as follows

- input : Student's full name
- output : email address in the format 'firstinitiallastname@gmail.com'
- the program removes spaces and special characters from the names for generation of email addresses
- duplicate emails are also handled
- resultant emails are saved in a new excel file

**Gender counter and logging**
The programs reads the student names and categorises them according to the 'Gender' column

- input : Student's full name ,student's gender
- output : A tsv and csv file of male students and that of female students
- a log file (students_log.log) will be created recording the number of male and female students

## Additional Notes

This program assumes the existence of 'Student Name' and 'Gender' column in your excel file
