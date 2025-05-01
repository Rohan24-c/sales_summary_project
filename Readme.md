# Sales Summary Project

This project is aimed at summarizing sales data using an SQLite database and visualizing the revenue per product through a bar chart. The task involves creating an SQLite database, inserting sample sales data, running a SQL query to summarize the data, and displaying the result with a bar chart.

## Project Structure

- **sales_summary.py**: The main Python script that creates the database, inserts data, runs the query, and generates a bar chart.
- **sales_data.db**: The SQLite database file that stores the sales data.
- **sales_chart.png**: The bar chart image showing revenue by product.
- **README.md**: This file, which explains the project.

## Steps

1. **Create the SQLite Database**:
   - The script connects to `sales_data.db`. If the database doesn’t exist, it is created automatically.
   - A `sales` table is created with columns: `id`, `product`, `quantity`, and `price`.

2. **Insert Sample Data**:
   - Sample sales data is inserted into the database. If the table is empty, the following data is used:
     - Laptop: 2 units at $700 each
     - Mouse: 10 units at $20 each
     - Keyboard: 5 units at $45 each
     - Laptop: 1 unit at $700
     - Mouse: 3 units at $20 each

3. **Run SQL Query**:
   - The script runs a query to calculate the total quantity and revenue per product. It groups the data by product and sums up the quantities and revenues.

4. **Generate Bar Chart**:
   - A bar chart is generated that visualizes the revenue for each product. The chart is saved as `sales_chart.png` and displayed on the screen.

## Requirements

- Python 3.x
- pandas
- matplotlib

Install the required libraries using:

```bash
pip install pandas matplotlib
