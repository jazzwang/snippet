import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import json

def calculate_headcount_trend(file_path):
    """
    Reads personnel data from a CSV, calculates the accumulated headcount 
    at the end of each month from Nov 2024 to Dec 2025, and outputs the result as JSON.

    Args:
        file_path (str): The path to the CSV file containing DOJ and LWD data.

    Returns:
        str: A JSON string containing the monthly headcount trend, or None on error.
    """
    
    # --- 1. Load and Clean Data ---
    
    if not os.path.exists(file_path):
        error_message = f"Error: File not found at path: {file_path}"
        print(error_message)
        return json.dumps({"error": error_message})

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
    except Exception as e:
        error_message = f"Error reading CSV file: {e}"
        print(error_message)
        return json.dumps({"error": error_message})

    # Standardize column names for easy access
    df.columns = df.columns.str.strip()
    
    # Check for mandatory columns
    required_cols = ['DOJ', 'LWD', 'Team']
    if not all(col in df.columns for col in required_cols):
        missing = [col for col in required_cols if col not in df.columns]
        error_message = f"Error: Missing required columns in CSV: {missing}"
        print(error_message)
        return json.dumps({"error": error_message, "missing_columns": missing})

    # Convert date columns to datetime objects. 
    date_format = '%m/%d/%Y' # Assuming M/D/YYYY format
    df['DOJ_dt'] = pd.to_datetime(df['DOJ'], format=date_format, errors='coerce')
    df['LWD_dt'] = pd.to_datetime(df['LWD'], format=date_format, errors='coerce')
    
    # Drop rows where DOJ is missing or invalid
    df.dropna(subset=['DOJ_dt'], inplace=True)
    
    # --- 2. Define Time Period ---
    
    # Start date: End of November 2024 (1st of Nov)
    start_date = datetime(2024, 11, 1) 
    # End date: December 2025 (we calculate up to the end of this month)
    end_date_limit = datetime(2025, 12, 31)

    # Generate a list of month-end dates to calculate headcount for
    month_ends = []
    current_month_start = start_date
    while current_month_start <= end_date_limit:
        # Get the last day of the current month
        next_month_start = current_month_start + relativedelta(months=1)
        month_end = next_month_start - relativedelta(days=1)
        
        # Append as datetime.datetime objects for direct comparison with pandas Timestamps
        month_ends.append(month_end)
        current_month_start = next_month_start

    # --- 3. Calculate Headcount for Each Month End, Grouped by Team ---

    unique_teams = df['Team'].unique()
    results = []

    for month_end_dt in month_ends: # Renamed 'date' to 'month_end_dt' for clarity
        month_data = {
            'month_end': month_end_dt.strftime('%Y-%m-%d'),
            'teams': {}
        }
        
        # Convert month_end_dt to pandas Timestamp for consistent comparison
        comparison_timestamp = pd.Timestamp(month_end_dt)

        # Calculate overall headcount for the month
        # DOJ_dt and LWD_dt are already pandas datetime64[ns]
        overall_joined = df['DOJ_dt'] <= comparison_timestamp
        # NaT values in LWD_dt will result in False for <= comparison, which is correctly handled by ~ operator
        overall_left = df['LWD_dt'] <= comparison_timestamp
        month_data['overall_headcount'] = df[overall_joined & ~overall_left].shape[0]

        for team in unique_teams:
            # Filter DataFrame for the current team
            # Using .copy() to ensure team_df is a distinct DataFrame, avoiding potential SettingWithCopyWarning
            team_df = df[df['Team'] == team].copy()

            # 1. Joined: DOJ must be ON or BEFORE the month_end date for the current team.
            joined = team_df['DOJ_dt'] <= comparison_timestamp
            
            # 2. Not Left: LWD must be missing (NaT) OR AFTER the month_end date for the current team.
            #    NaT values in LWD_dt will result in False for <= comparison, so ~(NaT <= comparison_timestamp) is True,
            #    correctly counting employees with no LWD as active.
            left = team_df['LWD_dt'] <= comparison_timestamp
            
            active_team_headcount = team_df[joined & ~left].shape[0]
            
            month_data['teams'][team] = active_team_headcount
        
        results.append(month_data)

    # --- 4. Output Results as JSON ---

    # Use json.dumps to convert the list of dictionaries into a formatted JSON string
    return json.dumps(results, indent=4)

# The name of the file to read.
CSV_FILE_NAME = "Data_Platform_Team_DOJ_LWD.csv"

if __name__ == "__main__":
    json_output = calculate_headcount_trend(CSV_FILE_NAME)
    
    # Print the final JSON string to the console
    if json_output:
        print(json_output)
