import json
import csv

def flatten_json(json_object, parent_key='', separator='_'):
    flat_dict = {}
    for key, value in json_object.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, new_key, separator=separator))
        else:
            flat_dict[new_key] = value
    return flat_dict

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    if 'results' in data and isinstance(data['results'], list) and all(isinstance(result, dict) for result in data['results']):
     
        flattened_data = [flatten_json(result) for result in data['results']]

        header = set(field for result in flattened_data for field in result.keys())

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)

            writer.writeheader()

            writer.writerows(flattened_data)
    
        print(f"Conversion successful. CSV file saved at {csv_file_path}")
    else:
        print("Invalid JSON format. Expecting a 'results' key with a list of dictionaries.")

#---------------------------------------------------------------#
def process_csv(file_path, selected_columns):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for col in selected_columns:
            if col not in reader.fieldnames:
                raise ValueError(f"Column '{col}' not found in the CSV file.")

        selected_data = [{col: row[col] for col in selected_columns} for row in reader]

    return selected_data

json_to_csv('modeb47-UBUNTU22-CIS-v1.0.0_post_scan_1704382231 copy.json', 'output5.csv')

if __name__ == "__main__":

    csv_file_path = "output5.csv"
    columns_to_select = ['skipped']     # Enter the columns to want 
    result_data = process_csv(csv_file_path, columns_to_select)
    print(result_data)
