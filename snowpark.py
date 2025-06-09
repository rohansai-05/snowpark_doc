

from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# Session Config
connection_parameters = {
    "account": "#####",
    "user": "###3",
    "password": "######",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "TEST",
    "schema": "TEST"
}

session = Session.builder.configs(connection_parameters).create()

data = [("Alice", 80), ("Bob", 90)]
df = session.create_dataframe(data, schema=["Name", "Score"])
df.show()

# Accessing an existing table
emp_df = session.table("employees")

# Show all data
print("Full Table:")
emp_df.show()

# Filter: Salary > 47000
print("Employees with Salary > 47000:")
emp_df.filter(col("salary") > 47000).show()

# Group by Dept and Avg Salary
print("Average Salary by Department:")
emp_df.group_by("deptno").agg({"salary": "avg"}).show()

# Select specific columns
print("Employee Names and Departments:")
emp_df.select("ename", "deptno").show()

# Sort by Salary Descending
print("Employees sorted by salary:")
emp_df.sort(col("salary").desc()).show()
