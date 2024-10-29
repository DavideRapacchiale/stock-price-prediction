import os
import pandas as pd
import random

# Define constants for folder paths
DATA_FOLDER = 'data'
OUTPUT_FOLDER = 'outputs'
EXCHANGE_FOLDERS = ['LSE', 'NASDAQ', 'NYSE']  # Specify folders for each exchange

def get_random_data_points(file_path, num_points=10):
    """
    Reads a stock CSV file, selects 10 consecutive data points from a random timestamp.
    Returns a DataFrame containing the sampled data points.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        df = pd.read_csv(file_path)
        
        # Check if the file is empty
        if df.empty:
            raise ValueError(f"File is empty: {file_path}")
        
        # Check if the file has at least 'num_points' rows
        if len(df) < num_points:
            print(f"Warning: File {file_path} has fewer than {num_points} rows; using available data.")
            return df  # Return all available data if fewer rows are present
        
        # Select a random starting index and return 10 consecutive data points
        start_idx = random.randint(0, len(df) - num_points)
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
        return [n_plus_1, n_plus_2, n_plus_3]
    
    except Exception as e:
        print(f"Error predicting values: {e}")
        return []  # Return empty list to signal failure

def process_exchange_files(exchange_folder, num_files=1):
    """
    Processes files in a given exchange folder, predicts values, and saves results.
    """
    try:
        # Ensure output directory exists
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        
        # Get list of CSV files in the exchange folder
        exchange_path = os.path.join(DATA_FOLDER, exchange_folder)
        files = [f for f in os.listdir(exchange_path) if f.endswith('.csv')]
        if len(files) == 0:
            print(f"No files found in directory: {exchange_folder}")
            return
        
        # Process each file up to the specified limit
        for file_name in files[:num_files]:
            file_path = os.path.join(exchange_path, file_name)
            
            # Step 1: Get 10 consecutive data points
            data_points = get_random_data_points(file_path)
            if data_points.empty:
                print(f"Skipping file {file_name} due to data retrieval issues.")
                continue  # Skip to the next file if data retrieval failed
            
            # Step 2: Predict the next 3 stock price values
            predictions = predict_next_3_values(data_points)
            if not predictions:
                print(f"Skipping file {file_name} due to prediction issues.")
                continue  # Skip to the next file if prediction failed
            
            # Step 3: Prepare output DataFrame and save to CSV
            output_df = data_points.copy()
            last_timestamp = pd.to_datetime(output_df['Timestamp'].iloc[-1], dayfirst=True)
            
            # Add predictions to the output
            for i, price in enumerate(predictions, start=1):
                new_timestamp = last_timestamp + pd.DateOffset(days=i)
                output_df = output_df.append({
                    'Stock-ID': output_df['Stock-ID'].iloc[0],
                    'Timestamp': new_timestamp.strftime('%d-%m-%Y'),
                    'Price': price
                }, ignore_index=True)
            
            # Save to a new CSV file in the outputs folder
            output_file = os.path.join(OUTPUT_FOLDER, f"{exchange_folder}_predicted_{file_name}")
            output_df.to_csv(output_file, index=False)
            print(f"Predictions saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while processing files in {exchange_folder}: {e}")

def generate_predictions(num_files=1):
    """
    Loops through each exchange folder and processes the specified number of files.
    """
    for exchange in EXCHANGE_FOLDERS:
        print(f"Processing exchange: {exchange}")
        process_exchange_files(exchange, num_files=num_files)

# Sample usage:
# generate_predictions(num_files=2)  # To process up to 2 files from each exchange folder
