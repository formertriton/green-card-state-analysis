import sqlite3
import pandas as pd
import os

def create_database():
    """Create SQLite database with schema"""
    # Connect to database (creates file if doesn't exist)
    conn = sqlite3.connect("data/green_card_analysis.db")
    cursor = conn.cursor()
    
    # Read schema file
    with open("sql/schema.sql", "r") as f:
        schema_sql = f.read()
    
    # Execute schema (create tables)
    cursor.executescript(schema_sql)
    
    # Commit and close
    conn.commit()
    conn.close()
    
    print("Database created successfully!")

def load_data_to_database():
    """Load processed CSV data into database"""
    # Read the processed data
    df = pd.read_csv("data/processed/green_card_data_clean.csv")
    
    # Connect to database
    conn = sqlite3.connect("data/green_card_analysis.db")
    
    # Insert data into table
    df.to_sql("green_card_admissions", conn, if_exists="replace", index=False)
    
    # Close connection
    conn.close()
    
    print(f"Loaded {len(df)} records into database!")

def test_database():
    """Test database with sample queries"""
    conn = sqlite3.connect("data/green_card_analysis.db")
    
    # Test query 1: Total records
    total = pd.read_sql("SELECT COUNT(*) as total FROM green_card_admissions", conn)
    print(f"Total records in database: {total['total'].iloc[0]}")
    
    # Test query 2: Top 5 states by total admissions
    top_states = pd.read_sql("""
        SELECT state, SUM(admissions) as total 
        FROM green_card_admissions 
        GROUP BY state 
        ORDER BY total DESC 
        LIMIT 5
    """, conn)
    print("\nTop 5 states by total admissions:")
    print(top_states)
    
    conn.close()

if __name__ == "__main__":
    print("Setting up database...")
    create_database()
    load_data_to_database()
    test_database()
print("Database setup complete!")