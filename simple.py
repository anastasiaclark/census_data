import requests

# in my plain text file there is only one line with the key
with open('census_api_key.txt') as key:
    api_key=key.read()

# variables
year='2017'
dataset_source='pep'
dataset_name='population'
variable='POP,GEONAME'
county='*'
state='44'

base_url = f'https://api.census.gov/data/'
data_url=f'{base_url}{year}/{dataset_source}/{dataset_name}?get={variable}&for=county:{county}&in=state:{state}&key={api_key}'

response=requests.get(data_url)
print(response.text)