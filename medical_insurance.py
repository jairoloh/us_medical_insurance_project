import csv

with open("insurance.csv") as insurace_file:
    patients_dict = {}
    csv_dict = csv.DictReader(insurance_file)

    for key,column in csv_dict:
        print["name"][5]
