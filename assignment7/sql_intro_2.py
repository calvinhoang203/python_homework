# Task 6: Read Data into a DataFrame
import pandas as pd
import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        # Create a DataFrame from a JOIN query
        sql_statement = """
        SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        """
        df = pd.read_sql_query(sql_statement, conn)

        # Print first 5 rows
        print("First 5 rows of the loaded DataFrame:")
        print(df.head())

        # Create a new 'total' column (quantity * price)
        df['total'] = df['quantity'] * df['price']
        print("\nFirst 5 rows after adding 'total' column:")
        print(df.head())

        # Group by product_id
        summary = df.groupby('product_id').agg(
            orders_count=('line_item_id', 'count'),
            total_revenue=('total', 'sum'),
            product_name=('product_name', 'first')
        )

        # Sort by product_name
        summary = summary.sort_values(by='product_name')

        # Print first 5 lines of the summary
        print("\nFirst 5 rows of the summary DataFrame:")
        print(summary.head())

        # Write to CSV
        summary.to_csv("order_summary.csv")
        print("\nSummary data written to 'order_summary.csv'.")

except Exception as e:
    print("Error working with database and pandas:", e)
