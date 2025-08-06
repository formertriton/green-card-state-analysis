-- Green Card Analysis Database Schema

-- Main table for green card admissions data
CREATE TABLE green_card_admissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(100) NOT NULL,
    year INTEGER NOT NULL,
    admissions INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster queries
CREATE INDEX idx_state_year ON green_card_admissions(state, year);
CREATE INDEX idx_country_year ON green_card_admissions(country, year);
CREATE INDEX idx_state_country ON green_card_admissions(state, country);

-- View for top countries by state (for our visualization)
CREATE VIEW top_countries_by_state AS
SELECT 
    state,
    country,
    SUM(admissions) as total_admissions,
    ROW_NUMBER() OVER (PARTITION BY state ORDER BY SUM(admissions) DESC) as country_rank
FROM green_card_admissions 
GROUP BY state, country;