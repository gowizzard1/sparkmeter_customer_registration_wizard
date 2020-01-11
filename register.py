import csv
import requests
import json
import os

def  registerFromcsvtoDictionary(file_name):
    with open(file_name + ".csv", encoding='utf-8-sig') as file:
        csv_file = csv.DictReader(file)
        count = 0
        for row in csv_file:
            resp = registercustomerTosparkmeter(dict(row))
            if resp.status_code != 201:
                print(resp.reason +'\n')
                print("***********The wizzard has registered " + str(count) + " customers**********")
                break
            print(dict(row))
            count += 1
            

def registercustomerTosparkmeter(customer):
    headers = {'Authentication-Token':os.environ.get('token')}
    payload = json.dumps(customer)
    r = requests.post(os.environ.get('url_api') + 'customer', data=payload, headers=headers)
    return r

file_name = input("Name of your csv file?: \n")
registerFromcsvtoDictionary(file_name)
