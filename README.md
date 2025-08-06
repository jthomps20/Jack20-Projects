# Jack20-Projects

## Overview

This repository contains demo backend projects built with Python Flask that showcase my skills in:

- Developing RESTful APIs
- Connecting to Snowflake cloud data warehouse
- Containerizing applications with Docker
- Deploying to AWS Elastic Kubernetes Service (EKS) with Kubernetes manifests

These projects demonstrate practical, real-world backend development, cloud deployment, and database integration.

---

## Projects

### 1. Cloud Demo Backend App

- A simple Flask web backend application.
- Containerized using Docker.
- Designed to be deployed on AWS EKS with Kubernetes (`deployment.yaml` and `service.yaml` included).
- Demonstrates how to build, containerize, and deploy a cloud-native app on AWS.

### 2. Flask-Snowflake-App

- Flask API server that connects to Snowflake using the official Snowflake Python connector.
- Loads connection credentials securely from environment variables.
- Exposes the following HTTP routes:
  - `/` — Returns a JSON greeting message.
  - `/error` — Triggers a test error to demonstrate error handling.
  - `/data` — Connects to Snowflake and queries `TEST_TABLE` (limited to 10 rows), returning results as JSON.
- Implements logging for all requests, errors, and Snowflake query operations.
- Includes global error handling to catch and log uncaught exceptions.

---

## Setup and Usage

### Prerequisites

- Python 3.10 or higher  
- pip  
- (Optional) Docker for containerization and deployment  
- (Optional) AWS CLI and kubectl for deploying to AWS EKS  
- Snowflake account with a database and table `TEST_TABLE` for the Flask-Snowflake app  

---

### Running Flask-Snowflake-App Locally

1. **Clone the repository**

    ```bash
    git clone https://github.com/jthomps20/Jack20-Projects.git
    cd Jack20-Projects/flask-snowflake-app
    ```

2. **Create a `.env` file** in the `flask-snowflake-app` directory containing your Snowflake credentials:

    ```ini
    SNOWFLAKE_USER=your_username
    SNOWFLAKE_PASSWORD=your_password
    SNOWFLAKE_ACCOUNT=your_account_name
    SNOWFLAKE_WAREHOUSE=your_warehouse
    SNOWFLAKE_DATABASE=your_database
    SNOWFLAKE_SCHEMA=your_schema
    ```

3. **Create and activate a Python virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask app**

    ```bash
    python app.py
    ```

6. **Access the API**

- Visit [http://localhost:5050/](http://localhost:5050/) for a simple greeting.  
- Visit [http://localhost:5050/data](http://localhost:5050/data) to fetch data from Snowflake’s `TEST_TABLE`.  
- Visit [http://localhost:5050/error](http://localhost:5050/error) to test error handling.

---

### Running Cloud Demo Backend App

Refer to the Dockerfile, Kubernetes manifests (`deployment.yaml`, `service.yaml`), and AWS EKS documentation for building, containerizing, and deploying this app to AWS.

---

## Notes

- The Snowflake connection defaults are overridden by environment variables for security.
- Ensure the `TEST_TABLE` exists in your Snowflake database with accessible data.
- Logging outputs to the console for info and error tracking.
- The Flask app listens on all interfaces at port 5050 (`0.0.0.0:5050`).

