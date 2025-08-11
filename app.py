import logging
import os
import snowflake.connector
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Snowflake connection config
SNOWFLAKE_CONFIG = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA')
}

def get_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG['user'],
        password=SNOWFLAKE_CONFIG['password'],
        account=SNOWFLAKE_CONFIG['account'],
        warehouse=SNOWFLAKE_CONFIG['warehouse'],
        database=SNOWFLAKE_CONFIG['database'],
        schema=SNOWFLAKE_CONFIG['schema']
    )

@app.route("/")
def home():
    logger.info("Home endpoint was reached")
    try:
        return jsonify({"message": "Hello from your Flask backend with Snowflake!"})
    except Exception as e:
        logger.error(f"Error in home endpoint: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/data")
def fetch_data():
    logger.info("Fetching data from Snowflake")
    try:
        conn = get_snowflake_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM TEST_TABLE LIMIT 10")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in rows]
            logger.info(f"Successfully fetched {len(results)} rows from Snowflake")
            return jsonify(results)
        except Exception as query_err:
            logger.error(f"Query failed: {query_err}", exc_info=True)
            return jsonify({"error": "Failed to execute query"}), 500
        finally:
            cursor.close()
            conn.close()
    except Exception as conn_err:
        logger.error(f"Snowflake connection failed: {conn_err}", exc_info=True)
        return jsonify({"error": "Failed to connect to Snowflake"}), 500

@app.route("/error")
def error():
    logger.info("Error route triggered")
    raise ValueError("This is a test error!")

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)
