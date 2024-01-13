#!/usr/bin/env python3

import pygsheets 
import pandas as pd

def make_df(wksht):
    data = wksht.get_all_values()

    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    nan_value = float("NaN") 
    
    df.replace("", nan_value, inplace=True) 
    #delete columns with no values
    df.dropna(how='all', axis=1, inplace=True) 
    #delete rows with no values
    df.dropna(how='all', axis=0, inplace=True) 

    print(df.to_string())
    return df

client = pygsheets.authorize(service_account_file='../attendance/key_2024') 
# opens a spreadsheet by its name/title
raw_sheet = client.open("Dues")
att_sheet = client.open("Spring 2024 Attendance")

#retreives a list of the names of individual worksheets
sheet_names = [s.title for s in raw_sheet.worksheets()]

# opens a worksheet by its name/title 
paid_wksht = raw_sheet.worksheet("title", "Paid") 
trips_wksht = raw_sheet.worksheet("title", "Trips") 
master_wksht = raw_sheet.worksheet("title", "Master") 
att_wksht = att_sheet.worksheet("title", "totals") 

paid_df = make_df(paid_wksht)
trips_df = make_df(trips_wksht)
master_df = make_df(master_wksht)
att_df = make_df(att_wksht)

#dict: {key=name: value = [owed, paid, trips, practices attended]}

DataFrame.to_dict(orient='dict', into=<class 'dict'>, index=True)