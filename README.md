# RentHub Listings Data Extraction

This Python project extracts real estate listings from the RentHub GraphQL API and processes the data into a flat structure before saving it as an Excel file. The script allows configuration via a JSON file (`config.json`) to specify API details, payload, headers, and output settings.


## Project Structure

. ├── main.py # The main Python script to run the project ├── config.json # JSON configuration file for API and output settings ├── requirements.txt # Python dependencies └── README.md # Project documentation

markdown
Copy code


## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pip` (Python package installer)


## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/renthub-listings-extraction.git
   cd renthub-listings-extraction|

2. Create a virtual environment (optional but recommended):

bash codes
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required packages:

bash codes
pip install -r requirements.txt


## Configuration

Before running the script, ensure that the config.json file is properly configured. This file contains:

API details such as the request URL, headers, and payload.
Output settings like the name of the Excel file.

Usage
1. Run the script:

bash codes
python main.py

2. The script will make a POST request to the RentHub API, retrieve the listings data, flatten the JSON response, and save the data to an Excel file as defined in the config.json file.


## Output

The script will output an Excel file containing the listings data with the following columns:

- `id`: The unique ID of the listing
- `name`: The name of the listing
- `province`: The province where the property is located
- `district`: The district of the property
- `subdistrict`: The subdistrict of the property
- `propertyType`: The type of the property (e.g., condo, apartment, etc.)
- `monthly_minPrice`: The minimum monthly rental price
- `monthly_maxPrice`: The maximum monthly rental price
- `daily_minPrice`: The minimum daily rental price (if applicable)
- `daily_maxPrice`: The maximum daily rental price (if applicable)


## Customization

You can modify the payload in the config.json file to filter by different zoneIds, rental terms, or other variables supported by the RentHub API. You can also adjust the output file name in the output section of the config.

## Dependencies

The Python dependencies for this project are listed in requirements.txt:


- requests
- pandas
- openpyxl

Install these dependencies using:

bash codes
pip install -r requirements.txt


## License
This project does not currently have a license. 
Please note that until a license is added, all rights are reserved, and no permissions are granted for use, distribution, or modification of this code.


## License
RentHub API for providing the data
Python community for the awesome tools and libraries
