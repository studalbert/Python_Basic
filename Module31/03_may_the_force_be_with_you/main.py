# TODO здесь писать код
import requests
import json

req = requests.get('https://www.swapi.tech/api/starships/12')
data = json.loads(req.text)
result_data = dict()
result_data['name'] = data['result']['properties']['name']
result_data['max_atmosphering_speed'] = data['result']['properties']['max_atmosphering_speed']
result_data['starship_class'] = data['result']['properties']['starship_class']
result_data['pilots'] = []


for elem in data['result']['properties']['pilots']:
    pilot = requests.get(elem)
    pilot_dict = json.loads(pilot.text)
    result_data['pilots'].append({'name': pilot_dict['result']['properties']['name'],
                                  'height': pilot_dict['result']['properties']['height'],
                                  'mass': pilot_dict['result']['properties']['mass'],
                                  'homeworld': pilot_dict['result']['properties']['homeworld']})

with open('result_data.json', 'w') as file:
    json.dump(result_data, file, indent=4)

json_data = json.dumps(result_data, indent=4)
print(json_data)