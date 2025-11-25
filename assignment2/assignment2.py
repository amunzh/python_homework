#TASK 2
import traceback
import csv
def read_employees():
    dict = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            emp_file = csv.reader(file)
            for i, row in enumerate(emp_file):
                if i == 0:
                    dict['fields'] = row[0:]
                else:
                    rows.append(row)
        dict['rows'] = rows
        return dict
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

employees = read_employees()
print(employees)

#TASK 3
def column_index(str):
    return employees["fields"].index(str)

employee_id_column = column_index("employee_id")

#TASK 4
def first_name(num):
    col_num = column_index('first_name')
    return employees['rows'][num][col_num]

#TASK 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#TASK 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#TASK 7
def sort_by_last_name():
    employees['rows'].sort(key = lambda row: row[column_index('last_name')])
    return employees['rows']

#TASK 8
def employee_dict(row):
    fields = employees['fields']
    dict = {}
    for i in range(1,len(fields)):
        dict[fields[i]] = row[i]
    return dict

test_row = employee_dict(employees['rows'][5])
print(test_row)

#TASK 9
def all_employees_dict():
    new_dict = {}
    for row in employees['rows']:
        new_dict[row[0]] = employee_dict(row)
    return new_dict
print(all_employees_dict())

#TASK 10
import os
def get_this_value():
    return os.getenv('THISVALUE')

#TASK 11
import custom_module
def set_that_secret(new_secret):
    return custom_module.set_secret(new_secret)
new_secr = set_that_secret('flowers')
print(custom_module.secret)

#TASK 12
def read_minutes():
    def read_file(file_name):
        dict = {}
        rows = []
        with open(file_name, 'r') as file:
            emp_file = csv.reader(file)
            for i, row in enumerate(emp_file):
                if i == 0:
                    dict['fields'] = row[0:]
                else:
                    rows.append(tuple(row))
            dict['rows'] = rows
            return dict
    minutes1 = read_file('../csv/minutes1.csv')
    minutes2 = read_file('../csv/minutes2.csv')
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(minutes1, '\n',  minutes2)

#TASK 13
def create_minutes_set():
    new_set = set(minutes1['rows']).union(set(minutes2['rows']))
    return new_set
minutes_set = create_minutes_set()

#TASK 14
from datetime import datetime
def create_minutes_list():
    list_set = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return list_set
minutes_list = create_minutes_list()
print(minutes_list)

#TASK 15
def write_sorted_list():
    minutes_list.sort(key = lambda x:x[1])
    new_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),minutes_list ))
    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        for row in new_list:
            writer.writerow(row)
    return new_list
sorted_list = write_sorted_list()
