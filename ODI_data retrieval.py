import os
import zipfile
import requests
import pandas as pd
import mysql.connector
from io import BytesIO
import json

# Function to download and extract the zip file
def download_and_extract_zip(zip_url, extract_path):
    response = requests.get(zip_url)
    with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref:
        zip_ref.extractall(extract_path)




zip_file_url = 'https://cricsheet.org/downloads/odis_json.zip'
zip_file_path = 'cricsheet_data.zip'
extraction_path = 'extracted_data'
download_and_extract_zip(zip_file_url, extraction_path)
print("file_Extracted")

# Combine all the json files

def combine_json_files(json_folder, output_json_path):
    # List to store contents of all JSON files
    combined_data = []

    # Iterate through each JSON file in the folder
    for json_file in os.listdir(json_folder):
        if json_file.endswith('.json'):

            json_path = os.path.join(json_folder, json_file)

            try:
                
                with open(json_path, 'r') as file:
                    json_content = json.load(file)
                    combined_data.append(json_content)

            except ValueError as ve:
                print(f"ValueError processing {json_file}: {ve}")
            except Exception as e:
                print(f"Error processing {json_file}: {e}")

    # Write the combined data to a new JSON file
    with open(output_json_path, 'w') as output_file:
        json.dump(combined_data, output_file, indent=2)

    print(f"Combined data written to {output_json_path}")


json_folder_path = 'extracted_data'
output_json_path = 'combined_data.json'

combine_json_files(json_folder_path, output_json_path)




#convert to csv
def csv_convert(combined_data_path):
    df = pd.read_json(combined_data_path)
    df.to_csv('file.csv')


combined_data_path  = "combined_data.json"

csv_convert(combined_data_path)
print("file converted")
