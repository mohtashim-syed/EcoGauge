import pandas as pd

# Input and output file paths
input_csv = "vehicles.csv"  # Replace with your original CSV file
output_csv = "vehicles_2021_2025.csv"  # The filtered output CSV file

def filter_vehicles(input_file, output_file):
    try:
        # Load the CSV file into a DataFrame
        print("Reading the input CSV file...")
        data = pd.read_csv(input_file)

        # Filter rows for vehicles manufactured between 2021 and 2025
        print("Filtering vehicles from 2021 to 2025...")
        filtered_data = data[(data['year'] >= 2021) & (data['year'] <= 2025)]

        # Save the filtered data to a new CSV file
        print(f"Saving the filtered data to {output_file}...")
        filtered_data.to_csv(output_file, index=False)

        print(f"Filtered data saved successfully to {output_file}!")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except KeyError:
        print("Error: The CSV file does not contain the required 'year' column.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the function
if __name__ == "__main__":
    filter_vehicles(input_csv, output_csv)

