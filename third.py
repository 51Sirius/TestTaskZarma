import json
import csv

with open('test.csv', mode='r') as file:
    data_csv = list(csv.reader(file))[1:]

with open('test.json', mode='r') as file:
    data_json = json.load(file)
for sale in data_json:
    for product in data_csv:
        if int(product[0]) == sale['product_id']:
            print(sale['product_id'], product[1], sale['sale_id'], sale['amount'])