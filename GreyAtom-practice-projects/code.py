# --------------
import numpy as np
import pandas as pd
import datetime as dt

bank = pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)


# --------------
# code starts here
banks=bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
print(bank_mode)
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],
values=['LoanAmount'],aggfunc='mean')
print(avg_loan_amount)

# code ends here


# mean value of 'Attack speed points' according to 'Generation' and 'Type 1'
# pivot=pd.pivot_table(df,index=['Type 1'],values=['Attack speed points'],columns=['Generation'])
# print(pivot)
# # Code ends here



# --------------
loan_approved_se=(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')
# print(banks[loan_approved_se])
loan_approved_nse=(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')
Loan_Status=614
percentage_se=banks[loan_approved_se]['Self_Employed'].count()*100/Loan_Status
percentage_nse=banks[loan_approved_nse]['Self_Employed'].count()*100/Loan_Status
print(percentage_se,'**',percentage_nse)


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
# print(loan_term)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)



# code ends here


# --------------
loan_groupby=banks.groupby(by=['Loan_Status'])
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
mean_values


