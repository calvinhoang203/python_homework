import csv
import traceback
import os
from datetime import datetime
import custom_module

# Task 2: Read a CSV File
def read_employees():
    
    # Empty dictionary to store CSV data
    employees_dict = {}
    
    # Empty list to store the rows (excluding the header)
    rows_list = []
    
    try:
        # Open the CSV file
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            
            # Loop through each row in the CSV file
            for index, row in enumerate(reader):
                if index == 0:
                    # Save the first row as the header fields
                    employees_dict["fields"] = row
                else:
                    # Add all other rows to the list
                    rows_list.append(row)
                    
        # Add the list of rows to the dictionary under the key "rows"
        employees_dict["rows"] = rows_list
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    # Return the employees' information
    return employees_dict

# Global variable that stores the returned value
employees = read_employees()
print("Employees data:", employees)


# Task 3: Find the Column Index

def column_index(column_name):
    # Return the index of the column in employees["fields"]
    return employees["fields"].index(column_name)

# Global variable that stores the column you get back
employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name

def first_name(row_number):
    # Get the column index for the first name column
    first_name_index = column_index("first_name")
    # Return the first name from the specified row
    return employees["rows"][row_number][first_name_index]



# Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    # Function that checks for a matching employee_id
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    # Use filter with the inner function to find matching rows
    matches = list(filter(employee_match, employees["rows"]))
    # Return the matches
    return matches




# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
    # Use a lambda function within filter to get matching rows
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches




# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    # Get the column index for last name
    last_name_index = column_index("last_name")
    # Sort employees["rows"] in place using lambda
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

print("Employees' last name sorted:", sort_by_last_name())


# Task 8: Create a dict for an Employee

def employee_dict(row):
    # Create a dictionary from a row with keys from employees["fields"]
    dict = {}
    for key, value in zip(employees["fields"], row):
        # Skip the 'employee_id' field
        if key != "employee_id":
            dict[key] = value
    return dict

print("Employee information in the first row:", employee_dict(employees["rows"][0]))
print("Employee information in the second row:", employee_dict(employees["rows"][1]))
print("Employee information in the third row:", employee_dict(employees["rows"][2]))


# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    # Create a dict where keys are employee_id values and values are employee dicts
    all_emp_dict = {}
    for row in employees["rows"]:
        id = row[employee_id_column]
        all_emp_dict[id] = employee_dict(row)
    return all_emp_dict

print("All employees info:", all_employees_dict())


# Task 10: Use the os Module

def get_this_value():
    # Return the value of the environment variable THISVALUE
    return os.getenv("THISVALUE")

print("THISVALUE:", get_this_value())


# Task 11: Creating Your Own Module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my_new_secret")
print("Custom module secret:", custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

# Helper Function
def read_csv_as_tuple(file_path):
    data_dict = {}
    rows_list = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data_dict["fields"] = row
                else:
                    rows_list.append(tuple(row))
        data_dict["rows"] = rows_list
        
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
    return data_dict


def read_minutes():
    minutes1 = read_csv_as_tuple('../csv/minutes1.csv')
    minutes2 = read_csv_as_tuple('../csv/minutes2.csv')
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print("Minutes1 data:", minutes1)
print("Minutes2 data:", minutes2)


# Task 13: Create minutes_set

def create_minutes_set():
    # Convert rows from minutes1 and minutes2 into sets and combine them
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined_set = set1.union(set2)
    return combined_set


minutes_set = create_minutes_set()
print("Combined minutes set:", minutes_set)


# Task 14: Convert to datetime

def create_minutes_list():
    # Convert the minutes_set into a list
    minutes_list_local = list(minutes_set)
    # Keep the name, and convert the date string to a datetime object
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_local))
    return converted_list


minutes_list = create_minutes_list()
print("Minutes list with datetime:", minutes_list)


# Task 15: Write Out Sorted List

def write_sorted_list():
    # Sort the minutes_list in ascending order by the datetime
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    # Convert each tuple back to a tuple with the date as a string
    converted_minutes = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))
    try:
        # Write the sorted data to a new CSV file
        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # Write the header from minutes1's fields
            writer.writerow(minutes1["fields"])
            # Write each row of the converted minutes list
            for row in converted_minutes:
                writer.writerow(row)
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    
    return converted_minutes

sorted_converted_minutes = write_sorted_list()
print("Sorted and converted minutes:", sorted_converted_minutes)