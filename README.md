<<<<<<< HEAD
# stock-price-prediction

Project Structure
The project structure is organized as follows:

bash
Copy code
stock-price-prediction/
├── data/               # Folder containing input CSV files organized by exchange
│   ├── LSE/
│   ├── NASDAQ/
│   └── NYSE/
├── outputs/            # Folder where the output files with predictions will be saved
├── stock_predictor.py  # Main Python script that performs data processing and prediction
├── requirements.txt    # List of required Python packages
└── README.md           # This README file
Folder and File Details
data/: Contains subfolders for each stock exchange (e.g., LSE, NASDAQ, NYSE). Each subfolder should contain CSV files with historical stock data.
outputs/: This folder is created automatically to save the output files with predictions.
stock_predictor.py: The main script where the data processing and prediction logic is implemented.
Setup
To set up the project and install the required dependencies, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
Install Dependencies: Install the required Python packages by running:

bash
Copy code
pip install -r requirements.txt
Prepare the Data: Place your CSV files in the appropriate subfolders inside the data/ directory (e.g., data/LSE, data/NASDAQ, data/NYSE). Each CSV file should have the following columns:

Stock-ID: A unique identifier for the stock.
Timestamp: The date in dd-mm-yyyy format.
Price: The stock price on that date.
Example CSV Format:

csv
Copy code
Stock-ID,Timestamp,Price
AAPL,01-01-2021,130.5
AAPL,02-01-2021,132.0
How It Works
The code is organized around the following main functions:

get_random_data_points(file_path, num_points=10):

This function selects 10 consecutive data points from a random starting point in a given file.
It reads the CSV file, verifies it contains sufficient data, and randomly chooses 10 consecutive rows.
Returns these rows as a DataFrame for further processing.
predict_next_3_values(data_points):

This function predicts the next 3 values in the stock price time series.
Prediction Logic:
n + 1: The second-highest value in the 10 selected data points.
n + 2: Calculated as the last known price plus half the difference between the last price and n + 1.
n + 3: Calculated as n + 2 plus a quarter of the difference between n + 1 and n + 2.
This function returns a list of the three predicted values.
process_exchange_files(exchange_folder, num_files=1):

Iterates through each file in the specified exchange folder and applies the above two functions.
Retrieves 10 random data points from each file, predicts the next 3 values, and saves the output in a new CSV file in the outputs/ folder.
Ensures that up to the specified number of files (num_files) are processed for each exchange.
generate_predictions(num_files=1):

This function loops through each exchange folder (LSE, NASDAQ, NYSE) and processes up to num_files from each folder.
Calls process_exchange_files for each exchange.
Flow of Execution
Generate Predictions: The generate_predictions(num_files) function is called as the entry point. This function accepts a parameter num_files, indicating the number of files to process per exchange.
File Processing: For each file, it retrieves 10 consecutive data points, predicts the next 3 values, and saves the results.
Output: The predictions for each file are saved in the outputs/ folder, with filenames indicating the exchange and stock file being processed.
Error Handling
The script is designed to handle common errors gracefully. Here’s a breakdown:

Missing or Empty Files: If a file is missing or empty, the script logs a warning and skips that file.
Insufficient Data: If a file has fewer than 10 data points, it uses whatever data is available.
Invalid Data Format: Checks if essential columns (like Price) are present. If not, it skips the file.
General Errors: Any unexpected errors are caught and logged without stopping the entire process.
Running the Application
Run the Script: To run the script, open the GitHub Codespaces terminal or your local terminal, navigate to the project directory, and enter:

bash
Copy code
python stock_predictor.py
Example Usage with Custom File Limit: To process up to 2 files from each exchange folder, you can modify the main script’s function call:

python
Copy code
generate_predictions(num_files=2)
Logs and Output:

The script prints status messages to the console, showing each file it processes and any errors or warnings.
Predictions are saved in outputs/, named according to the exchange and file name.
Output Format
Each processed file will have a corresponding output file in the outputs/ folder. The output format matches the input format, with 10 original data points followed by the 3 predicted values.

Example Output File
Each row in the output file has the following format:

csv
Copy code
Stock-ID,Timestamp,Price
AAPL,01-01-2021,130.5
AAPL,02-01-2021,132.0
...
AAPL,11-01-2021,133.0
AAPL,12-01-2021,134.5
AAPL,13-01-2021,135.0
Explanation:

Stock-ID: Identifier of the stock.
Timestamp: Original and predicted timestamps.
Price: Original prices and predicted values.
The predicted values are appended after the 10 original data points, with each timestamp incremented by one day.

Notes and Assumptions
Simple Prediction Model: The model uses a rule-based approach. For a real-world application, a more sophisticated model (e.g., ARIMA, LSTM) might yield better accuracy.
Date Formatting: Assumes dates in dd-mm-yyyy format.
Modularity: Functions are modular to allow easy updates or extensions.
=======

>>>>>>> eb546f7e37cd9ba0aed8668fc743f023dcf1e513