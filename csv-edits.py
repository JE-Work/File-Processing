#!/bin/usr/env python3

# A script to make simple changes to an existing CSV file of 100k plus rows.
# Changes being looked for:
# 1. Change the existing header row names to other names that are supplied.
# 2. Create a new column to contain data from another and alter the data to a time object.
# 3. Filter a column's data to only contain a full URL.

import datetime as dt
import pandas as pd

# FUNCTION TO CONVERT DATA FROM BOKLANGD1
def get_num(item):
    num = ""
    for d in item:
        if d.isdigit():
            num = num + d
    h, m = divmod(int(num), 100)
    return dt.time(hour=h, minute=m)

# FUNCTION TO PULL OUT ONLY URL FROM COLUMN 
def get_url(href):
    link = href.split('src="')[1].split('">')[0]
    return link

# IMPORT THE FILE
data = pd.read_csv('test.csv')

# CHANGE COLUMN HEADER NAMES   
HEADERS = ['bokurl', 'boknamn', 'forfattare', 'betyg', 'boklangd1', 'sidor', 'upplasare', 'finns-som', 'kategori1', 'kategori2', 'kategori3', 'kategori4', 'kategori5', 'kategori6', 'bokbeskrivning', 'bild', 'sprak', 'datum', 'isbn', 'copyright1', 'copyright2', 'URL Encoded Address']
data.columns = HEADERS

# ADD NEW COLUMN & POPULATE IT USING GET_NUM FUNCTION
data.insert(5, 'boklangd2', data['boklangd1'].apply(get_num))

# POPLUATE BILD COLUMN WITH ONLY THE URL VALUE
data['bild'] = data['bild'].apply(get_url)

# DISPLAY SAMPLE ROW TO CONFIRM DATA CHANGES
#print(data.iloc[0])
