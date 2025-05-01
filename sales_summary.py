import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create the sales table (if it doesn't already exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Save changes and close connection
conn.commit()
# Step 3: Insert sample data if the table is empty
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ('Laptop', 2, 700.00),
        ('Mouse', 10, 20.00),
        ('Keyboard', 5, 45.00),
        ('Laptop', 1, 700.00),
        ('Mouse', 3, 20.00)
    ]
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
    conn.commit()

# Step 4: Close the connection
conn.close()
# Step 5: Reconnect to the database to run a query
conn = sqlite3.connect("sales_data.db")
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Step 6: Load the results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 7: Close the connection
conn.close()

# Step 8: Print the results
print("Sales Summary:")
print(df)
# Step 9: Plot a bar chart for total revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()  # Adjust layout to make sure everything fits
plt.show()
# Step 10: Save the chart as a PNG image (optional)
plt.savefig("sales_chart.png")
