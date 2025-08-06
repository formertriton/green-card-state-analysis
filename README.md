# Green Card State Analysis

Interactive visualization of US green card recipients by state and country of origin (2018-2023).

<img width="1226" height="766" alt="Screenshot 2025-08-05 233240" src="https://github.com/user-attachments/assets/5a1742d7-c733-4fb0-80f7-04dfc428c531" />
<img width="1099" height="788" alt="Screenshot 2025-08-05 233308" src="https://github.com/user-attachments/assets/dd17d417-a0e4-4481-a289-26eded4de0a1" />

## Project Overview

This project analyzes lawful permanent resident (green card) data from the Department of Homeland Security to create an interactive map visualization showing immigration patterns across US states.

## Technologies Used

- **Python**: Data collection, cleaning, and processing
- **SQL**: Data storage and querying
- **D3.js**: Interactive map visualization
- **Pandas**: Data manipulation and analysis
- **SQLite/PostgreSQL**: Database management

## Data Source

Data sourced from the Office of Homeland Security Statistics (OHSS):
- New Lawful Permanent Residents by State, County, Country of Birth (2018-2023)
- Official DHS immigration statistics

## Project Structure
```
green-card-state-analysis/
├── data/
│   ├── raw/           # Original downloaded data files
│   └── processed/     # Cleaned and processed data
├── src/
│   ├── data_collection.py
│   ├── data_processing.py
│   └── database.py
├── sql/
│   └── schema.sql
├── web/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── requirements.txt
└── README.md
```


## Features

- Interactive US map with hover functionality
- State-level green card recipient counts
- Top 3 countries of origin per state
- Time series analysis (2018-2023)
- Responsive web design

## Status

🚧 **In Development** - This project is actively being built as a portfolio piece.

---

*This project demonstrates skills in data analysis, database design, web development, and data visualization.*

<img width="319" height="247" alt="Screenshot 2025-08-05 234040" src="https://github.com/user-attachments/assets/cef871c7-7ab4-4bf7-aaa3-813077f27d0d" />

<img width="481" height="389" alt="Screenshot 2025-08-05 234052" src="https://github.com/user-attachments/assets/9c757b82-3290-4bf6-9c09-5548f3f845aa" />
