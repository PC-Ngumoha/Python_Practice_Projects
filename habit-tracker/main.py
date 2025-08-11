import requests
from datetime import datetime

TOKEN = 'dl;aklkdks;lfkflpweo'
USERNAME = 'pcngumoha'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': "Reading Graph",
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji',
}

auth_headers = {
    'X-USER-TOKEN': TOKEN,
}

# Creating the graph
# response = requests.post(graph_endpoint, headers=auth_headers, json=graph_config)
# response.raise_for_status()
# print(response.status_code)

# Adding a new pixel to the graph.
add_pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
today = datetime.now()
# pages_read = input('Enter number of pages read today: ')

# pixel_payload = {
#     'date': today.strftime('%Y%m%d'), # Today's date in the format: yyyyMMdd
#     'quantity': pages_read,
# }


# response = requests.post(add_pixel_endpoint, headers=auth_headers, json=pixel_payload)
# response.raise_for_status()
# if response.status_code == 200:
#     print('Entry recorded successfully')

# chosen_date = input('Enter date to update (yyyyMMdd): ')
# update_pixel_endpoint = f'{add_pixel_endpoint}/{chosen_date}'
# pages_read = input(f'Enter number of pages actually read on {chosen_date}: ')

# payload = {
#     'quantity': pages_read,
# }

# response = requests.put(update_pixel_endpoint, headers=auth_headers, json=payload)
# response.raise_for_status()
# print(response.text)

chosen_date = input('Enter date to delete (yyyyMMdd): ')
delete_pixel_endpoint = f'{add_pixel_endpoint}/{chosen_date}'

response = requests.delete(delete_pixel_endpoint, headers=auth_headers)
response.raise_for_status()
print(response.text)
