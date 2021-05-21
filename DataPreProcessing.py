import csv

data_1 = []
data_2 = []
with open("DataPreProcessing.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
       data_1.append(row)
headers =data_1[0]
planet_data =data_1[1:]
for data_1_point in planet_data:
   data_1_point[2] =data_1_point[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2])
with open("DataPrepping.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csv.writerows(planet_data)

for row in csvreader:
        data_2.append(row)
headers = data_2[0]
planet_data_2 = data_2[1:]
for data_2_point in planet_data:
    data_2_point[2] = data_2_point[2].lower()
planet_data_2.sort(key = lambda planet_data:planet_data[2])
with open("DataPrepping.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csv.writerows(planet_data)
