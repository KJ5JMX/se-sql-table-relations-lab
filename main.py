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
    SELECT firstName, lastName, jobTitle
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
df_credit = pd.read_sql(""" SELECT firstName, lastName, COUNT(customers.customerNumber) AS num_customers FROM employees JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber WHERE customers.creditLimit >90000 GROUP BY employees.employeeNumber ORDER BY num_customers DECS """, conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT productName, COUNT(orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits FROM orderdetails JOIN products ON orderdetails.productCode = products.productCode GROUP BY products.productCode ORDER BY totalunits DESC """, conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.sql_read("""
                                 SELECT productName, products.productCode, COUNT(DISTINCT customers.customerNumber) AS numpurchasers FROM orderdetails
                                 JOIN products ON orderdetails.productCode = products.productCode
                                 JOIN orders ON orderdetails.orderNumber = orders.orderNumber
                                 JOIN customers ON orders.customerNumber = customers.customerNumber
                                 GROUP BY products.productCode
                                 ORDER BY numpurchasers DESC """, conn) 

# STEP 9
# Replace None with your code
df_customers = pd.sql_read("""
                           SELECT officeCode, city, COUNT(customerNumber) AS n_customers FROM customers
                           JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber
                           JOIN offices ON employees.officeCode = offices.officeCode
                           GROUP BY offices.officeCode """, conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
                          SELECT employeeNumber, firstName, lastName, city, officeCode FROM employees
                          JOIN offices ON employees.officeCode = offices.officeCode
                          WHERE employeeNumber IN (
                          SELECT COUNT(DISTINCT customers.customerNumber) AS numpurchasers FROM orderdetails
                                 JOIN products ON orderdetails.productCode = products.productCode
                                 JOIN orders ON orderdetails.orderNumber = orders.orderNumber
                                 JOIN customers ON orders.customerNumber = customers.customerNumber
                                 JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber
                                 GROUP BY products.productCode
                                 ORDER BY numpurchasers DESC HAVING numpurchasers < 20) """, conn)
                          
conn.close()