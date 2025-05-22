import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        # Step 1: Read JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Step 2: Ensure it's a list of dictionaries
        if not isinstance(data, list):
            raise ValueError("JSON must be a list of dictionaries.")

        # Step 3: Write to CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"✅ Conversion successful! CSV saved as: {csv_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Call the function with file names
json_to_csv('data.json', 'output.csv')
