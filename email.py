import pandas as pd
import re

# Load the data from the Excel file
df = pd.read_excel(r'TestFiles.xlsx')

# Function to generate email address by splitting names...
def generate_email(name):
    # Names are split via re.sub()
    # [^a-zA-Z\s] removes whitespaces or special characters
    clean_name = re.sub(r'[^a-zA-Z\s]', '', name)
    parts = clean_name.split()
    
    # Extract the first character of the first name and last name
    if len(parts) == 1:
        email = f"{parts[0].lower()}@gmail.com"
    else:
        email = f"{parts[0][0].lower()}{parts[-1].lower()}@gmail.com"
    
    return email

# Apply the function to generate email addresses
#Check for duplicates and if found, append a number to distinguish
df['Email'] = df['Student Name'].apply(generate_email)

# Ensure uniqueness of email addresses after removing whitespaces
df['Email'] = df['Email'].apply(lambda x: re.sub(r'\s+', '', x))
df['Email'] = df['Email'].apply(lambda x: x if pd.isna(df['Email'].where(df['Email'] == x).count()) else x[:-10] + str(df['Email'].where(df['Email'] == x).count()) + "@gmail.com")

# Save the updated data to a CSV file
df.to_csv('students_with_emails.csv', index=False)
