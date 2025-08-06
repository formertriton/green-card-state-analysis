from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import pandas as pd

app = Flask(__name__)
CORS(app)  # This allows requests from any origin

@app.route('/api/states')
def get_all_states():
    """Get list of all states"""
    conn = sqlite3.connect("data/green_card_analysis.db")
    states = pd.read_sql("SELECT DISTINCT State FROM green_card_admissions ORDER BY State", conn)
    conn.close()
    return jsonify(states['State'].tolist())

@app.route('/api/state/<state_name>')
def get_state_data(state_name):
    """Get top 3 countries for a specific state"""
    conn = sqlite3.connect("data/green_card_analysis.db")
    query = """
        SELECT Country, SUM(Admissions) as total
        FROM green_card_admissions 
        WHERE State = ?
        GROUP BY Country 
        ORDER BY total DESC 
        LIMIT 3
    """
    top_countries = pd.read_sql(query, conn, params=[state_name])
    
    total_query = "SELECT SUM(Admissions) as total FROM green_card_admissions WHERE State = ?"
    total = pd.read_sql(total_query, conn, params=[state_name])
    
    conn.close()
    
    return jsonify({
        'state': state_name,
        'total_admissions': int(total['total'].iloc[0]),
        'top_countries': top_countries.to_dict('records')
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)