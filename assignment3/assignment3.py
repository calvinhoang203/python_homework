import pandas as pd



# Task 1
# Create a dictionary

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary to a dataframe
df = pd.DataFrame(data)

# Print the dataframe
print("Dataframe:\n", df)

# Save the dataframe in a variable called task1_data_frame
task1_data_frame = df

# Make a copy of the dataframe
task1_with_salary = task1_data_frame.copy()

# Add a column called Salary with values [70000, 80000, 90000]

task1_with_salary = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000]
})

# Print the new dataframe
print("Dataframe with salary:\n", task1_with_salary)

# Make a copy of task1_with_salary in a variable named task1_older
task1_older = task1_with_salary.copy()

# Increment the Age column by 1 for each entry.
task1_older['Age'] = task1_older['Age'] + 1

# Print the modified dataframe
print("Modified dataframe:\n", task1_older)

# Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file
task1_older.to_csv('employees.csv', index=False)



# Task 2

# Load the data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print("Employees Data:\n", task2_employees)

# Create a JSON file (additional_employees.json) and add new data into json file
additional_employees = pd.DataFrame({
    'Name': ['Eve', 'Frank'],
    'Age': [28,40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000,95000]
})
additional_employees.to_json('additional_employees.json', index = False)

# Load this JSON file into a new DataFrame and assign it to the variable json_employees
json_employees = pd.read_json('additional_employees.json')
print("Additional employees Data (Json):\n", json_employees)

# Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Combined data:\n", more_employees)


# Task 3

# Assign the first three rows of the more_employees DataFrame to the variable first_three
first_three = more_employees.head(3)
print("First three rows of the combined data:\n", first_three)

# Assign the last two rows of the more_employees DataFrame to the variable last_two
last_two = more_employees.tail(2)
print("Last two rows of the combined data:\n", last_two)

# Assign the shape of the more_employees DataFrame to the variable employee_shape
employee_shape = more_employees.shape
print("The shape of the combined data:\n", employee_shape)

# Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts
employee_info = more_employees.info
print("Summary of the combined data:\n", employee_info)


# Task 4

# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')

print('Dirty data:\n', dirty_data)

# Create a copy of the dirty data in the varialble clean_data
clean_data = dirty_data.copy()

print('Clean data:\n', clean_data)

# Remove any duplicate rows
clean_data = clean_data.drop_duplicates()
print('Clean data without duplicates:\n', clean_data)

# Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")
print('Clean data with age conversion and missing values handled:\n', clean_data)

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")
clean_data['Salary'] = clean_data['Salary'].replace('unknown', pd.NA)
clean_data['Salary'] = clean_data['Salary'].replace('n/a', pd.NA)
print('Clean data with salary conversion and placeholder handled:\n', clean_data)

# Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data['Age'].mean()
median_salary = clean_data['Salary'].median()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
print('Clean data with missing numeric values handled:\n', clean_data)

# Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce")
print('Clean data with hire data conversion:\n', clean_data)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print('Clean data with extra whitespace and uppercase handled:\n', clean_data)

