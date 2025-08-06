import pandas as pd
import os

def process_single_file(filepath, year):
    """Process a single data file"""
    print(f"\n=== Processing {filepath} ===")
    
    # Load and clean data (reusing our logic)
    if filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath, skiprows=3)
    else:
        df = pd.read_csv(filepath, skiprows=3)
    
    df.columns = ['State', 'County', 'Country', 'Class_of_Admission', 'Admissions']
    df = df[df['State'] != 'State of Residence']
    df = df.reset_index(drop=True)
    
    print(f"Original shape: {df.shape}")
    
    # Remove 'D' values (our key decision)
    df = df[df['Admissions'] != 'D']
    print(f"After removing 'D' values: {df.shape}")
    
    # Convert Admissions to numeric
    df['Admissions'] = pd.to_numeric(df['Admissions'])
    
    # Add year column
    df['Year'] = year
    
    # Aggregate by State and Country (sum across counties and admission classes)
    state_country_totals = df.groupby(['State', 'Country', 'Year'])['Admissions'].sum().reset_index()
    
    print(f"Aggregated to state-country level: {state_country_totals.shape}")
    
    return state_country_totals

def process_all_files():
    """Process all LPR files"""
    data_dir = "data/raw/"
    files = [f for f in os.listdir(data_dir) if f.startswith('lpr_')]
    
    all_data = []
    
    for file in files:
        # Extract year from filename (assuming lpr_2018.xlsx format)
        year = file.split('_')[1].split('.')[0]
        filepath = os.path.join(data_dir, file)
        
        processed_df = process_single_file(filepath, int(year))
        all_data.append(processed_df)
    
    # Combine all years
    combined_df = pd.concat(all_data, ignore_index=True)
    
    print(f"\n=== FINAL COMBINED DATA ===")
    print(f"Total records: {combined_df.shape}")
    print(f"Years covered: {sorted(combined_df['Year'].unique())}")
    print(f"States/territories: {combined_df['State'].nunique()}")
    print(f"Countries: {combined_df['Country'].nunique()}")
    
    # Save processed data
    output_path = "data/processed/green_card_data_clean.csv"
    combined_df.to_csv(output_path, index=False)
    print(f"\nSaved to: {output_path}")
    
    return combined_df

if __name__ == "__main__":
    df = process_all_files()
    
    # Quick preview
    print("\nSample of final data:")
    print(df.head(10))
    
    print("\nProcessing complete!")