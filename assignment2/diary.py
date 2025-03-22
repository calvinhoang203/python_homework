# Task 1: Diary

import traceback

try:
    # Open the file diary.txt
    with open("diary.txt", "a") as file:
        prompt = "What happened today? "  # First prompt
        while True:
            # Get input from the user
            line = input(prompt)
            # Write the input to the file with a newline at the end
            file.write(line + "\n")
            # If the special exit line is entered, exit
            if line == "done for now":
                break
            # Change prompt for subsequent inputs
            prompt = "What else? "
            
except Exception as e:
    print("An exception occurred.")
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
