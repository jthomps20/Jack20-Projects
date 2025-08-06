import snowflake.connector

# Optional: Print connector version
print(snowflake.connector.__version__)

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='JTHOMPS20',
    password='Elmo873476028!',
    account='porhomv-qsb41605',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_SAMPLE_DATA',
    schema='TPCH_SF1'
)

# Create a cursor object
cur = conn.cursor()

# Execute a simple query
cur.execute("SELECT * FROM CUSTOMER LIMIT 5")

# Fetch and print results
for row in cur.fetchall():
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

