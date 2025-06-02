# Task 1: Plotting with Pandas
# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data from SQLite database
conn = sqlite3.connect('../db/lesson.db')
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id
"""
# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query, conn)
conn.close()


# Display the DataFrame
df.plot(kind='bar', x='last_name', y='revenue', color='skyblue', title='Employee Revenue')
plt.xlabel('Employee')
plt.ylabel('Revenue')
plt.show()