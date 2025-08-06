import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for detailed logs or INFO for normal
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.route("/")
def home():
    logger.info("Home endpoint was reached")
    try:
        # Your usual response here
        return jsonify({"message": "Hello from your Flask backend!"})
    except Exception as e:
        # Log any unexpected error with traceback
        logger.error(f"Error in home endpoint: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

# Optional: Test error route to check error handling and logging
@app.route("/error")
def error():
    logger.info("Error route triggered")
    raise ValueError("This is a test error!")

# Global error handler - catches any unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    # Run on port 5050 as before, with debug off
    app.run(host="0.0.0.0", port=5050, debug=False)
