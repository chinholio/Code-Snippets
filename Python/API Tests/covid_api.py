import requests
import json
import pandas as pd

url = 'https://covid-19-statistics.p.rapidapi.com/reports/total'
params = {'date': '2020-04-07'}
headers = {
            'x-rapidapi-host': 'covid-19-statistics.p.rapidapi.com',
            'x-rapidapi-key': '0510b8ed98mshc1dc586963910e7p104896jsn0255b9f45530'
            }
response = requests.request("GET", url, params=params, headers=headers)

parsed_data = json.loads(response.text)

def flatten_json(json):
    dict1 = {}   
   
    def flatten(i, name=''):      
        if type(i) is dict:
            for a in i:
             flatten(i[a], name + '_' + a + '')
        else:
            dict1[name[:-1]] = i
    flatten(json)
    return dict1
   
df = pd.DataFrame.from_dict(flatten_json(parsed_data), orient='index')

print(df)