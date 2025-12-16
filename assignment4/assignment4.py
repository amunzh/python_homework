import pandas as pd
#TASK 1
#part 1
data_t1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data_t1)
print(task1_data_frame)

#part 2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

#part 3
task1_older = task1_with_salary.copy()
task1_older['Age'] +=1
print(task1_older)

#part 4
task1_older.to_csv("employees.csv", index=False)


#TASK 2
#part 1
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

#part 2
new_emp = {
    'Name': ['Eve','Frank'],
    'Age': [28,40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]
}
df_new_emp = pd.DataFrame(new_emp)
df_new_emp.to_json('additional_employees.json')
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

#part 3
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


#TASK 3
#part 1
first_three = more_employees.head(3)
print(first_three)
#part 2
last_two = more_employees.tail(2)
print(last_two)
#part 3
employee_shape = more_employees.shape
print(employee_shape)
#part 4
more_employees.info()


#TASK 4
#part 1
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()

#part 2
clean_data = clean_data.drop_duplicates()
print(clean_data)

#part 3
clean_data['Age'] = pd.to_numeric(clean_data['Age'],errors="coerce")
print(clean_data)

#part 4
clean_data['Salary'] = clean_data['Salary'].replace('unknown', pd.NA)
clean_data['Salary'] = clean_data['Salary'].replace('n/a', pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'],errors="coerce")
print(clean_data)

#part 5
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Age'].fillna(clean_data['Age'].median())
print(clean_data)

#part 6
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format = "mixed", errors="coerce")
print(clean_data)

#part 7
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Department'] = clean_data['Department'].str.upper()
print(clean_data)