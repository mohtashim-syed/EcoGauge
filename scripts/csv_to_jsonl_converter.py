import pandas as pd
import json

# Input and output file paths
input_csv = "vehicles_2021_2025.csv"
output_jsonl = "toyota_vehicle_details.jsonl"  # Output JSONL file

def generate_prompt(row):
    """Generate a user prompt based on the row data."""
    return (
        f"What are the details of the {int(row['year'])} {row['make']} {row['model']}? "
        "Include fuel economy, engine specs, and class."
    )

def generate_completion(row):
    """Generate a detailed assistant completion based on the row data."""
    return (
        f"The {int(row['year'])} {row['make']} {row['model']} features a {row['cylinders']}-cylinder engine "
        f"with a displacement of {row['displ']} liters. It offers a combined fuel economy of {row['comb08']} MPG, "
        f"a city fuel economy of {row['city08']} MPG, and a highway fuel economy of {row['highway08']} MPG. "
        f"This vehicle uses {row['fuelType']} fuel and has a {row['drive']} drivetrain. "
        f"It belongs to the {row['VClass']} vehicle class."
    )

try:
    # Load the filtered CSV
    data = pd.read_csv(input_csv)

    # Prepare JSONL data
    with open(output_jsonl, "w") as jsonl_file:
        for _, row in data.iterrows():
            # Construct the JSON object for each row
            json_obj = {
                "messages": [
                    {"role": "user", "content": generate_prompt(row)},
                    {"role": "assistant", "content": generate_completion(row)}
                ]
            }
            # Write the JSON object to the JSONL file
            jsonl_file.write(json.dumps(json_obj) + "\n")

    print(f"JSONL file created successfully: {output_jsonl}")

except FileNotFoundError:
    print(f"Error: The file '{input_csv}' was not found. Please ensure it's in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")

