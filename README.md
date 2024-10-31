Stock Price Prediction
======================

This script processes historical stock data for various exchanges (LSE, NASDAQ, NYSE), generates future price predictions based on a simple extrapolation formula, and saves the results as new CSV files in an output directory.

Folder Structure
----------------

The project folder contains:

*   **Data**: Folder containing subfolders for each exchange (LSE, NASDAQ, NYSE) with CSV files representing stock data.
    
*   **Outputs**: Folder where the output files with predictions are saved.
    
*   **Main script**: Contains the code that performs data processing and prediction.
    

### File Requirements

*   Each input CSV file in the Data subfolders (e.g., Data/LSE/FLTR LSE.csv) must contain at least 10 rows of historical stock data.
    
*   Expected columns in each file:
    
    *   **Stock-ID**: Unique identifier for the stock.
        
    *   **Timestamp**: Date of each record in DD-MM-YYYY format.
        
    *   **Price**: Closing price of the stock on that date.
        

Functions Overview
------------------

### get\_random\_data\_points(file\_path, num\_points=10)

*   **Purpose**: Reads a specified CSV file and extracts 10 consecutive data points starting from a random timestamp.
    
*   **Parameters**:
    
    *   file\_path (str): Path to the stock data CSV file.
        
    *   num\_points (int, optional): Number of consecutive data points to retrieve (default is 10).
        
*   **Returns**: A DataFrame containing the sampled data points or an empty DataFrame if an error occurs.
    

### predict\_next\_3\_values(data\_points)

*   **Purpose**: Predicts the next 3 prices based on the provided 10 data points.
    
*   **Parameters**:
    
    *   data\_points (DataFrame): DataFrame containing the 10 sampled stock prices.
        
*   **Returns**: A list containing 3 predicted price values.
    

### process\_exchange\_files(exchange\_folder, num\_files=1)

*   **Purpose**: Processes each file in a specified exchange folder, generates predictions, and saves the results to the output directory.
    
*   **Parameters**:
    
    *   exchange\_folder (str): Name of the folder containing files for a specific stock exchange.
        
    *   num\_files (int, optional): Number of files to process in each folder (default is 1).
        
*   **File Output**: Saves a new CSV file with the predictions in the Outputs folder.
    

### generate\_predictions(num\_files=1)

*   **Purpose**: Main function that iterates through each exchange folder (LSE, NASDAQ, NYSE) and processes a specified number of files.
    
*   **Parameters**:
    
    *   num\_files (int, optional): Number of files to process per exchange folder (default is 1).
        

Usage
-----

To generate predictions for stock prices, call the generate\_predictions function. For example, to process up to 2 files per exchange folder:

`   generate_predictions(num_files=2)   `

**This will:**

1.  Retrieve 10 random data points from each file.
    
2.  Predict the next 3 price values based on a simple extrapolation formula.
    
3.  Save the original data along with the predictions in a new CSV file in the Outputs folder.
    

Error Handling
--------------

*   If a file is missing, empty, or does not meet the row requirement, an error message is printed, and the file is skipped.
    
*   If the expected columns (Stock-ID, Timestamp, Price) are missing, the script will raise an error and skip the file.