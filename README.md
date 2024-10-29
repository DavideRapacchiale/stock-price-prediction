Stock Price Prediction
======================

This project predicts the next 3 stock price values based on historical data using a rule-based approach. The application processes CSV files for different stock exchanges and generates predictions based on a simple statistical model.

Project Structure
-----------------

*   **stock\_predictor.py**: Main script that retrieves data, generates predictions, and saves output.
    
*   **data/**: Folder where input CSV files are stored, containing subfolders for each stock exchange:
    
    *   LSE/
        
    *   NASDAQ/
        
    *   NYSE/
        
*   **outputs/**: Folder where the prediction results are saved as CSV files.
    
*   **requirements.txt**: List of required Python packages.
    

Requirements
------------

*   Python 3.x
    
*   pandas: Install using the command: pip install pandas
    

Setup Instructions
------------------

### Step 1: Clone the Repository

Clone the repository to your local machine by running:git clone [https://github.com/your-username/stock-price-prediction.git](https://github.com/your-username/stock-price-prediction.git)cd stock-price-prediction

### Step 2: Install Dependencies

Install the required packages by running:pip install -r requirements.txt

### Step 3: Add Data Files

1.  Place your stock data CSV files in the data/ directory, organized by exchange folders:
    
    *   data/LSE/
        
    *   data/NASDAQ/
        
    *   data/NYSE/
        
2.  Each CSV file should have the following columns:
    
    *   **Stock-ID**: Unique identifier for the stock.
        
    *   **Timestamp**: Date in dd-mm-yyyy format.
        
    *   **Price**: Stock price for that date.

3.  Example CSV data format:Stock-ID,Timestamp,PriceAAPL,01-01-2021,130.5AAPL,02-01-2021,132.0
    
### Step 4: Create the Outputs Folder

An outputs/ folder will be created automatically to store the prediction results. If it does not already exist, the script will generate it.

Running the Application
-----------------------

Run the main script to generate predictions by processing files from each exchange folder.

By default, the generate\_predictions function processes up to 1 file from each exchange folder, but you can adjust this as needed.

Run the script using:python stock\_predictor.py

To specify the number of files to process from each exchange folder (e.g., 2 files), adjust the following line in the script:generate\_predictions(num\_files=2)

Each processed file generates a CSV in the outputs/ folder containing the original 10 data points and 3 additional predictions.

### Example Output Format

Each output CSV file follows this format:Stock-ID,Timestamp,PriceAAPL,01-01-2021,130.5AAPL,02-01-2021,132.0...AAPL,11-01-2021,131.5AAPL,12-01-2021,133.0AAPL,13-01-2021,134.5

Prediction Model
----------------

The prediction logic is as follows:

1.  The first predicted value (n + 1) is the second-highest value among the last 10 data points.
    
2.  The second predicted value (n + 2) is half the difference between n (the last known price) and n + 1.
    
3.  The third predicted value (n + 3) is one-fourth the difference between n + 1 and n + 2.
    

This model provides a simple estimation based on recent price trends.

Error Handling
--------------

The application includes error handling for common issues:

*   File Not Found: Checks if the specified files and folders exist.
    
*   Empty Files: Handles cases where files are empty or contain no valid data.
    
*   Missing Columns: Ensures that the required Price column is present.
    
*   General Exceptions: Catches and logs unexpected errors without stopping the program
