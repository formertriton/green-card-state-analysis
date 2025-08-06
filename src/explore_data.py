import pandas as pd
import os

def explore_single_file(filepath):
    """Explore a single data file"""
    print(f"\n=== Exploring {filepath} ===")
    
    # Load the data with proper headers
    if filepath.endswith('.xlsx'):
        # Skip first 3 rows and use row 3 as headers
        df = pd.read_excel(filepath, skiprows=3)
    else:
        df = pd.read_csv(filepath, skiprows=3)
    
    # Set proper column names based on what we see
    df.columns = ['State', 'County', 'Country', 'Class_of_Admission', 'Admissions']
    
    # Remove the header row that got mixed in with data
    df = df[df['State'] != 'State of Residence']
    
    # Reset index after removing rows
    df = df.reset_index(drop=True)
    
    print(f"Shape after cleaning: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nFirst 10 rows:")
    print(df.head(10))
    print("\nData types:")
    print(df.dtypes)
    
    return df

def analyze_data_quality(df):
    """Analyze data quality issues"""
    print("\n=== DATA QUALITY ANALYSIS ===")
    
    # Check for 'D' values
    d_count = (df['Admissions'] == 'D').sum()
    print(f"Rows with 'D' (non-disclosure): {d_count}")
    
    # Check for missing values
    print(f"\nMissing values per column:")
    print(df.isnull().sum())
    
    # Look at unique states
    print(f"\nTotal unique states: {df['State'].nunique()}")
    print(f"Sample states: {sorted(df['State'].unique())[:15]}")
    
    # Look at admission values
    print(f"\nAdmissions column sample values:")
    print(df['Admissions'].value_counts().head(10))
    
    return df

# Main exploration
if __name__ == "__main__":
    data_dir = "data/raw/"
    files = [f for f in os.listdir(data_dir) if f.startswith('lpr_')]
    
    for file in files:
        filepath = os.path.join(data_dir, file)
        df = explore_single_file(filepath)
        df = analyze_data_quality(df)  # This was missing!
        break  # Just do first file for now

print("Data exploration complete!")