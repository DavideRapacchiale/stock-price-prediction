import os
import pandas as pd
import random

# Define constants for folder paths and specific file paths
OUTPUT_FOLDER = 'Outputs'
FILE_PATHS = {
    'LSE_FLTR': 'Data/LSE/FLTR LSE.csv',
    'LSE_GSK': 'Data/LSE/GSK LSE.csv',
    'NASDAQ_TSLA': 'Data/NASDAQ/TSLA.csv',
    'NYSE_ASH': 'Data/NYSE/ASH.csv',
    'NYSE_NMR': 'Data/NYSE/NMR.csv'
}
# Define column names to use when reading files without headers
COLUMN_NAMES = ['Stock-ID', 'Timestamp', 'Price']

def get_random_data_points(file_path, num_points=10):
    """
    Reads a stock CSV file, selects 10 consecutive data points from a random timestamp.
    Returns a DataFrame containing the sampled data points.
    """
    try:
        print(f"Attempting to read file: {file_path}")
        
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Read CSV file without assuming headers and assign column names
        df = pd.read_csv(file_path, header=None, names=COLUMN_NAMES)
        
        # Check if the file is empty
        if df.empty:
            raise ValueError(f"File is empty: {file_path}")
        
        # Check if the file has at least 'num_points' rows
        if len(df) < num_points:
            print(f"Warning: File {file_path} has fewer than {num_points} rows; using available data.")
            return df  # Return all available data if fewer rows are present
        
        # Select a random starting index and return 10 consecutive data points
        start_idx = random.randint(0, len(df) - num_points)
        print(f"Selected data points starting at index {start_idx} from file: {file_path}")
        return df.iloc[start_idx:start_idx + num_points]
    
    except Exception as e:
        print(f"Error retrieving data points from file {file_path}: {e}")
        return pd.DataFrame()  # Return empty DataFrame to signal failure

def predict_next_3_values(data_points):
    """
    Predicts the next 3 values based on the provided 10 data points.
    Returns a list of predictions.
    """
    try:
        if data_points.empty or 'Price' not in data_points.columns:
            raise ValueError("Data points are empty or do not contain a 'Price' column.")
        
        # Sort prices to find the second highest value
        sorted_prices = sorted(data_points['Price'].values)
        n_plus_1 = sorted_prices[-2]  # 2nd highest value
        n = data_points['Price'].iloc[-1]  # Last known price
        
        # Calculate predictions using the given formula
        n_plus_2 = n + (n_plus_1 - n) / 2
        n_plus_3 = n_plus_2 + (n_plus_1 - n_plus_2) / 4
        print(f"Predicted values: {n_plus_1}, {n_plus_2}, {n_plus_3}")
        return [n_plus_1, n_plus_2, n_plus_3]
    
    except Exception as e:
        print(f"Error predicting values: {e}")
        return []  # Return empty list to signal failure

def process_file(file_key, file_path):
    """
    Processes a specific file, predicts values, and saves results.
    """
    try:
        # Ensure output directory exists
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        
        print(f"Processing file: {file_path}")
        
        # Step 1: Get 10 consecutive data points
        data_points = get_random_data_points(file_path)
        if data_points.empty:
            print(f"Skipping file {file_path} due to data retrieval issues.")
            return  # Skip if data retrieval failed
        
        # Step 2: Predict the next 3 stock price values
        predictions = predict_next_3_values(data_points)
        if not predictions:
            print(f"Skipping file {file_path} due to prediction issues.")
            return  # Skip if prediction failed
        
        # Step 3: Prepare output DataFrame and save to CSV
        output_df = data_points.copy()
        last_timestamp = pd.to_datetime(output_df['Timestamp'].iloc[-1], dayfirst=True)
        
        # Add predictions to the output
        for i, price in enumerate(predictions, start=1):
            new_timestamp = last_timestamp + pd.DateOffset(days=i)
            prediction_row = pd.DataFrame({
                'Stock-ID': [output_df['Stock-ID'].iloc[0]],
                'Timestamp': [new_timestamp.strftime('%d-%m-%Y')],
                'Price': [price]
            })
            output_df = pd.concat([output_df, prediction_row], ignore_index=True)
        
        # Construct output path with proper naming
        output_file = os.path.join(OUTPUT_FOLDER, f"{file_key}.csv")
        output_df.to_csv(output_file, index=False)
        print(f"Predictions saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while processing file {file_path}: {e}")

def generate_predictions(num_files=1):
    """
    Loops through each specified file path and processes the specified number of files.
    """
    count = 0
    for file_key, file_path in FILE_PATHS.items():
        if count >= num_files:
            break
        print(f"Starting processing for: {file_path}")
        process_file(file_key, file_path)
        count += 1

# Sample usage:
generate_predictions(num_files=3)  # Adjust the number of files to process as needed
