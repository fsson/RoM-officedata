import pandas as pd
import json
import os

# Function for flattening and concatenating JSON data
def clean_json_files(file_paths):
    merged_data = None
    for path in file_paths:
        # Cut date from file name
        date = str(path[-15:-5])
        # Load and clean data
        with open(path, 'r') as file:
            data = json.load(file)
            # Turn data into dataframe
            df = pd.DataFrame(data)
            # Explode and normalize by supplier
            df = pd.json_normalize(df.explode("leverantorer")["leverantorer"])
            # Explode by address
            df = df.explode("adresser")
            # Create new dataframe for normalized address information
            adresses = pd.json_normalize(df["adresser"])
            # Drop address and index from original dataframe
            df = df.drop(columns=["adresser"]).reset_index(drop=True)
            # Concatenate add address information to original dataframe
            df = pd.concat([df, adresses], axis=1)
            # Add date column
            df["observerad_datum"] = date
        # Append data to master dataframe
        if merged_data is None:
            merged_data = df
        else:
            merged_data = pd.concat([merged_data, df], axis=0)
    return merged_data

# Function for creating CSV
def create_csv():
    # Create list of files
    filenames = [os.path.join("data/raw/", filename) for filename in os.listdir("data/raw/")]
    # Apply function to files
    df = clean_json_files(filenames)
    # Write data to CSV
    df.to_csv("data/clean/full_data.csv", index=False)
    print("CSV successfully created.")