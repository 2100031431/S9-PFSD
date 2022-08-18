import csv

with open('persons.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)