import sqlite3


def main():
    # connect to the database (adjust path if needed)
    conn = sqlite3.connect("../db/lesson.db", isolation_level='IMMEDIATE')
    # enable foreign key checks
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1: Complex JOINs with Aggregation
    print("Task 1")
    cursor.execute(
        """
        SELECT o.order_id,
               SUM(li.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """
    )
    for order_id, total_price in cursor.fetchall():
        print(f"Order ID: {order_id}, Total Price: {total_price}")
    print()

    # Task 2: Understanding Subqueries
    print("Task 2")
    cursor.execute(
        """
        SELECT c.customer_name,
               AVG(sub.total_price) AS avg_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id   AS customer_id_b,
                   SUM(li.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS sub
          ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id;
        """
    )
    for customer, avg_price in cursor.fetchall():
        print(f"Customer: {customer}, Average Total Price: {avg_price}")
    print()

    # Task 3: An Insert Transaction Based on Data
    print("Task 3")
    try:
        conn.execute("BEGIN")

        # fetch the customer_id for Perez and Sons
        cursor.execute(
            "SELECT customer_id FROM customers WHERE customer_name = ?;",
            ("Perez and Sons",)
        )
        row = cursor.fetchone()
        if not row:
            raise RuntimeError("Customer 'Perez and Sons' not found")
        customer_id = row[0]

        # fetch the employee_id for Miranda Harris
        cursor.execute(
            "SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?;",
            ("Miranda", "Harris")
        )
        row = cursor.fetchone()
        if not row:
            raise RuntimeError("Employee 'Miranda Harris' not found")
        employee_id = row[0]

        # get the 5 least expensive products
        cursor.execute(
            "SELECT product_id FROM products ORDER BY price ASC LIMIT 5;"
        )
        product_ids = [r[0] for r in cursor.fetchall()]

        # insert a new order and get its order_id
        cursor.execute(
            "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id;",
            (customer_id, employee_id)
        )
        order_id = cursor.fetchone()[0]

        # insert 10 of each selected product
        for pid in product_ids:
            cursor.execute(
                "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
                (order_id, pid, 10)
            )

        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    else:
        # display the newly inserted line items
        cursor.execute(
            """
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?;
            """,
            (order_id,)
        )
        print("New line items:")
        for lid, qty, pname in cursor.fetchall():
            print(f"  Line Item ID: {lid}, Quantity: {qty}, Product: {pname}")
    print()

    # Task 4: Aggregation with HAVING
    print("Task 4")
    cursor.execute(
        """
        SELECT e.employee_id, e.first_name, e.last_name,
               COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5;
        """
    )
    for emp_id, first, last, count in cursor.fetchall():
        print(f"Employee ID: {emp_id}, Name: {first} {last}, Orders: {count}")

    conn.close()


if __name__ == "__main__":
    main()
