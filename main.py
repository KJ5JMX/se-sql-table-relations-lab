# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
    SELECT firstName, lastName
    FROM employees
    JOIN offices ON employees.officeCode = offices.officeCode
    WHERE offices.city = "Boston"
""", conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
    SELECT * FROM offices
    LEFT JOIN employees ON offices.officeCode = employees.officeCode
    GROUP BY offices.officeCode
    HAVING COUNT(employees.employeeNumber) = 0
""", conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
                          SELECT firstName, lastName, city, state FROM employees JOIN offices ON employees.officeCode = offices.officeCode
                          ORDER BY firstName ASC, lastName ASC """, conn)

                          

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber FROM customers LEFT JOIN orders ON customers.customerNumber = orders.customerNumber
                          WHERE orders.orderNumber IS NULL ORDER BY contactLastName ASC
""", conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
                         SELECT contactFirstName, contactLastName, CAST(amount AS FLOAT), paymentDate FROM customers JOIN payments ON customers.customerNumber = payments.customerNumber
                         ORDER BY CAST(amount AS FLOAT) DESC """, conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT employees.employeeNumber, employees.firstName, employees.lastName, COUNT(customers.customerNumber) AS num_customers
    FROM employees
    JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
    GROUP BY employees.employeeNumber
    HAVING AVG(customers.creditLimit) > 90000
    ORDER BY num_customers DESC
""", conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT productName, COUNT(orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits FROM orderdetails JOIN products ON orderdetails.productCode = products.productCode GROUP BY products.productCode ORDER BY totalunits DESC """, conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
                                 SELECT productName, products.productCode, COUNT(DISTINCT customers.customerNumber) AS numpurchasers FROM orderdetails
                                 JOIN products ON orderdetails.productCode = products.productCode
                                 JOIN orders ON orderdetails.orderNumber = orders.orderNumber
                                 JOIN customers ON orders.customerNumber = customers.customerNumber
                                 GROUP BY products.productCode
                                 ORDER BY numpurchasers DESC """, conn) 

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
                           SELECT offices.officeCode, offices.city, COUNT(customerNumber) AS n_customers FROM customers
                           JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber
                           JOIN offices ON employees.officeCode = offices.officeCode
                           GROUP BY offices.officeCode """, conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
    SELECT DISTINCT employees.employeeNumber, employees.firstName, employees.lastName, offices.city,offices.officeCode FROM employees
    JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
    JOIN orders  ON customers.customerNumber = orders.customerNumber
    JOIN orderdetails  ON orders.orderNumber = orderdetails.orderNumber
    JOIN offices  ON employees.officeCode = offices.officeCode
    WHERE orderdetails.productCode IN (
        SELECT products.productCode
        FROM orderdetails
        JOIN orders USING (orderNumber)
        JOIN customers USING (customerNumber)
        JOIN products USING (productCode)
        GROUP BY products.productCode
        HAVING COUNT(DISTINCT customers.customerNumber) < 20
    )
                          ORDER BY employees.firstName, employees.lastName ASC
""", conn)
                          
conn.close()