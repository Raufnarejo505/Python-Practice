import pandas as pd 

emp_name = pd.Series(['Ali','Rasool','Bux'], name = 'names')
emp_emails = pd.Series(['ali.gmai','rasool.gmail','names.gmail'], name = 'emails')
emp_phones = pd.Series(['0231','0341','0342'], name = 'phones')

emp_DF = pd.concat([emp_name, emp_emails, emp_phones], axis=1)

print(emp_DF)
