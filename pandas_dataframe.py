import pandas as pd 
data = [['9001','Ali','Sales'],
        ['9002','ayub','Sales'],
        ['9003','saleem','Sales']]
emps = pd.DataFrame(data, columns = ['Emp_no', 'Name', 'Job'])
column_types = {'Emp_no' : int, 'Name': str, 'Job' : str}
emps = emps.astype(column_types)
emps = emps.set_index('Emp_no')

# print(emps)

# joining two DataFrames connected with a one-to-one relationnship
salary_data = [ ['9001','3000'],
                ['9002','2000'],
                ['9003','2500']]
salary = pd.DataFrame(salary_data, columns = ['Emp_no', 'Salary'])
salary_columns = {'Emp_no' : int, 'Salary' : int}
salary = salary.astype(salary_columns)
salary = salary.set_index('Emp_no')

# new_emp = pd.Series({'Name' : 'Hasnain' , 'Job' : 'Sales'}, name = '9004')
# emps = emps._append(new_emp)
# # print(emps)

# Emp_salary = emps.join(salary)
# # print(Emp_salary)

# # Exercise #04 using different joins
# new_data =  pd.Series({'Salary' : '5000'}, name = 9009)
# salary = salary._append(new_data)
# # emp_salary = emps.join(salary, how='left')
# emp_salary = emps.join(salary, how='outer')
# print(emp_salary)


# One to many joins
data_orders = [[2608, 9001, 35],
          [2617, 9001, 35],
          [2620, 9001, 139],
          [2621, 9002, 95],
          [2626, 9002, 218]]

orders = pd.DataFrame(data_orders, columns=['Phono', 'Emp_no', 'Total'])
emp_orders = emps.merge(orders, how = 'inner', left_on='Emp_no', right_on='Emp_no').set_index('Phono')
# print(emp_orders)

# aggregating the Data with groupby()
print(orders.groupby(['Emp_no'])['Total'].mean())  # mean function 
print(orders.groupby(['Emp_no'])['Total'].sum())   # sum function


