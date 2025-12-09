#TASK 3
import csv
data_list = []
with open('./csv/employees.csv', 'r') as file:
            emp_file = csv.reader(file)
            for row in emp_file:
                data_list.append(row)

emp_names = [f'{row[1]} {row[2]}' for i,row in enumerate(data_list) if i != 0]
print(emp_names)

e_names = [row for row in emp_names if 'e' in row.lower()]
print(e_names)