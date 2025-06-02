# Task 2: A Line Plot with Pandas
# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


# Load data from SQLite database
conn = sqlite3.connect('../db/lesson.db')
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
"""
# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Display the DataFrame
df.plot(x='order_id', y='cumulative', kind='line', title='Cumulative Revenue')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.show()

# Task 3: Interactive Plotly Visualization
# Load libraries
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace('[^0-9.]', '', regex=True).astype(float)

fig = px.scatter(df, x='strength', y='frequency', color='direction', title='Wind Strength vs Frequency')
fig.write_html("wind.html", auto_open=True)