import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")
#the newline="" is telling the script that each new line is
#indicated by a blank because the csv has none in each line
with open(cereal_csv,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        if float(row[7])>=5:
            print(row)