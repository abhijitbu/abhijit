# import pandas as pd

# # Assuming df_200 is your DataFrame (you can load it from an Excel file or create it manually)
# # Example: loading from the Excel file generated earlier
# #df_200 = pd.read_excel('C:/Users/Abhijit/Desktop/employee_data_200.xlsx')
# df_200 = pd.read_excel('C:/Users/Abhijit/Desktop/employee_data_200.xlsx')


# for index, row in df_200.iterrows():
#     sql = f"INSERT INTO employees (first_name, last_name, email, phone_number, position, department, hire_date, salary) " \
#           f"VALUES ('{row['First Name']}', '{row['Last Name']}', '{row['Email']}', '{row['Phone Number']}', " \
#           f"'{row['Position']}', '{row['Department']}', '{row['Hire Date']}', {row['Salary']});"
#     print(sql)
import pandas as pd

# Load the data (upload the Excel file or load it from your system)
df_200 = pd.read_excel('C:/Users/Abhijit/Desktop/employee_data_200.xlsx')

for index, row in df_200.iterrows():
    sql = f"INSERT INTO employees (first_name, last_name, email, phone_number, position, department, hire_date, salary) " \
          f"VALUES ('{row['First Name']}', '{row['Last Name']}', '{row['Email']}', '{row['Phone Number']}', " \
          f"'{row['Position']}', '{row['Department']}', '{row['Hire Date']}', {row['Salary']});"
    print(sql)
