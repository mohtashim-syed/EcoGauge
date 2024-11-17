import pandas as pd

# Load dataset
file_path = "vehicles.csv"  # Replace with your actual file path

try:
    # Read the CSV file
    vehicles_data = pd.read_csv(file_path)

    # Filter for Toyota vehicles between 2021-2025
    toyota_data = vehicles_data[
        (vehicles_data['make'] == 'Toyota') & 
        (vehicles_data['year'] >= 2021) & 
        (vehicles_data['year'] <= 2025)
    ]

    # Select and process relevant fields
    toyota_trimmed_data = toyota_data[['year', 'model', 'city08', 'highway08', 'comb08']].copy()

    # Create 'trim' field from the 'model' column
    toyota_trimmed_data['trim'] = toyota_trimmed_data['model'].apply(
        lambda x: ' '.join(x.split(' ')[1:]) if isinstance(x, str) else ''
    )

    # Save the filtered data to a new CSV file
    output_file = "toyota_updated.csv"
    toyota_trimmed_data.to_csv(output_file, index=False)

    print(f"Filtered data saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it's in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")
