import pandas as pd
import sqlite3

# TASK 1
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
query = ''' 
SELECT orders.order_id, SUM(line_items.quantity*products.price)
FROM orders 
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id LIMIT 5;
'''
cursor.execute(query)
print(cursor.fetchall())
cursor.close()
conn.close()

#TASK 2
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
query = ''' 
SELECT customers.customer_name, AVG(total_price) as average_total_price
FROM customers 
LEFT JOIN 
    (
        SELECT  orders.customer_id AS customer_id_b, SUM(line_items.quantity*products.price) AS total_price
       FROM orders 
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id 
   ) ON customer_id = customer_id_b
GROUP BY customers.customer_id;
'''
cursor.execute(query)
print(cursor.fetchall())
cursor.close()
conn.close()

#TASK 3
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()
query1 = ''' 
INSERT INTO orders (customer_id,employee_id)
VALUES ((SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'),
        (SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'))
RETURNING order_id;''' 

query2 = ''' 
INSERT INTO line_items (order_id, product_id, quantity)
SELECT ?,
    product_id,
    10
FROM products ORDER BY price LIMIT 5;
'''
cursor.execute(query1)
id = cursor.fetchone()[0]
cursor.execute(query2,(id,))
cursor.execute('''SELECT line_item_id,quantity,product_name
                FROM line_items
                JOIN products ON line_items.product_id = products.product_id
                WHERE line_items.order_id = ?; ''',(id,))
print(cursor.fetchall())
cursor.close()
conn.close()

#TASK 4
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
query = ''' 
SELECT first_name, last_name, COUNT(o.order_id)
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 4;
'''
cursor.execute(query)
print(cursor.fetchall())
cursor.close()
conn.close()
