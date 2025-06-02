# Task 3: List Comprehensions Practice
import pandas as pd

df = pd.read_csv("../csv/employees.csv")

# Create list of full names
names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print(names)

# Names containing 'e'
names_with_e = [name for name in names if 'e' in name.lower()]
print(names_with_e)
