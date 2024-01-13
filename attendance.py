#!/usr/bin/env python3

import pygsheets 
import pandas as pd


client = pygsheets.authorize(service_account_file='../attendance/key_2024') 
# opens a spreadsheet by its name/title

raw_sheet = client.open("Spring 2024 Attendance")

sheet_names = [s.title for s in raw_sheet.worksheets()]
print(sheet_names)

# opens a worksheet by its name/title 
zero_worksht = raw_sheet.worksheet("title", sheet_names[0]) 


data = zero_worksht.get_all_values()
print(type(data))

headers = data.pop(0)
print(headers)
df = pd.DataFrame(data, columns=headers)
df.rename(columns={"Attendees\nEnter as a list separated by line returns (no bullet points)": "Attendees"}, inplace=True)
nan_value = float("NaN") 
 
df.replace("", nan_value, inplace=True) 
df.dropna(how='all', axis=1, inplace=True) 
print(df.columns)
print(df.to_string())