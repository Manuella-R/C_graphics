import pandas as pd
import re


df = pd.read_excel(r'TestFiles.xlsx')


def generate_email(name):
    clean_name = re.sub(r'[^a-zA-Z\s]', '', name)
    parts = clean_name.split()
    
    if len(parts) == 1:
        email = f"{parts[0].lower()}@gmail.com"
    else:
        email = f"{parts[0][0].lower()}{parts[-1].lower()}@gmail.com"
    
    return email

df['Email'] = df['Student Name'].apply(generate_email)

df['Email'] = df['Email'].apply(lambda x: re.sub(r'\s+', '', x))
df['Email'] = df['Email'].apply(lambda x: x if pd.isna(df['Email'].where(df['Email'] == x).count()) else x[:-10] + str(df['Email'].where(df['Email'] == x).count()) + "@gmail.com")

df.to_csv('students_with_emails.csv', index=False)
