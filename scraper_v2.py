import requests
import pandas as pd
import json

# Load the configuration from the JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Extract necessary values from the config
url = config['api_details']['url']
headers = config['api_details']['headers']
payload = json.dumps(config['api_details']['payload'])
output_file = config['output']['file_name']

# Step 1: Fetch data from the API
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
else:
    raise Exception(f"API request failed with status code {response.status_code}")

# Step 2: Extract and process the JSON data
listings = data['data']['listings']['result']

# Flatten the JSON structure
flattened_listings = []

for listing in listings:
    flattened = {
        'id': listing.get('id'),
        'name': listing.get('name'),
        'province': listing.get('province'),
        'district': listing.get('district'),
        'subdistrict': listing.get('subdistrict'),
        'propertyType': listing.get('propertyType'),
        'monthly_minPrice': listing.get('price', {}).get('monthly', {}).get('minPrice'),
        'monthly_maxPrice': listing.get('price', {}).get('monthly', {}).get('maxPrice'),
        'daily_minPrice': listing.get('price', {}).get('daily', {}).get('minPrice'),
        'daily_maxPrice': listing.get('price', {}).get('daily', {}).get('maxPrice')
    }
    flattened_listings.append(flattened)

# Step 3: Convert the flattened list of listings to a DataFrame
df = pd.DataFrame(flattened_listings)

# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Data successfully written to {output_file}")
