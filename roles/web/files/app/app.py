from flask import Flask, jsonify
import os
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Load database connection info from environment variables
DB_HOST = os.environ.get("DB_HOST", "192.168.77.144")
DB_USER = os.environ.get("DB_USER", "fidan")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "ubuntu")
DB_NAME = os.environ.get("DB_NAME", "app")

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            ssl_disabled=True
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    conn = get_connection()
    if conn is None:
        return jsonify({"status": "error", "message": "Failed to connect to database"}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT NOW() AS `current_time`;")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "time": result["current_time"]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
