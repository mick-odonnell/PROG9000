import requests
import csv
import os

#data = requests.get(
#                 "http://airo.maynoothuniversity.ie/files/dDATASTORE/crime/" +
#                 "garda%20stations/garda_stations.csv")

save_dir = "C:\\Users\\Admin\\PycharmProjects\\DT9426\\week5\\data"
fn = "crime_data.csv"

p = os.path.join(save_dir, fn)

#with open(p, 'wb') as file_obj:
#    file_obj.write(data.content)
    
with open(p, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
        
