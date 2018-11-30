import requests
import csv

path = "C:\\Users\\admin\\OneDrive\\GIS\\DataDump\\CSO_2016\\Commuting_data.csv"

with open(path, "r") as csv_file_object:
    dr = csv.DictReader(csv_file_object)
    r = csv.reader(csv_file_object)

    row_list = []
    for row in dr:
        row_list.append(row)

    simple_reader_list = []

    for row in r:
        simple_reader_list.append(row)

num_rows = len(row_list)

item1 = row_list[0]
num_cols = len(item1)

field_names = item1.keys()

col_dict = {}

for fn in field_names:
    col_dict[fn] = []

for row in row_list:
    for col_name in field_names:
        col_dict[col_name].append(row[col_name])
