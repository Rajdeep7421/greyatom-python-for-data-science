# --------------

# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# step 1
# code starts here

bank = pd.read_csv(path)

# Create the variable 'categorical_var' and using 'df.select_dtypes(include = 'object')' check all categorical values.
categorical_var=bank.select_dtypes(include='object')

print(categorical_var)

# Create the variable 'numerical_var' and using 'df.select_dtypes(include = 'number')' check all categorical values
numerical_var=bank.select_dtypes(include='number')

# =============
print('='*50)


print(numerical_var)
# code ends here


# step 2
# code starts here

# From the dataframe bank, drop the column Loan_ID to create a new dataframe banks
banks= bank.drop(columns='Loan_ID')


# To see the null values, use "isnull().sum()" function

print(banks.isnull().sum())

# Calculate mode for the dataframe banks

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# ============
print('='*50)
# check if all the missing values filled.

print(banks.isnull().sum())


# code ends here
print('='*50)

# step 3
# Code starts here

# Generate a pivot table with index and store result
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print (avg_loan_amount)

# code ends here

print('='*50)

# step 4
# code starts here

# store the count of results where Self_Employed == Yes and Loan_Status == Y.
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

print('='*50)

# store the count of results where Self_Employed == No and Loan_Status == Y
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

print('='*50)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]

print(percentage_se)

print('='*50)
#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]

print (percentage_nse)


# code ends here
print('='*50)

#step 5
# code starts here

# convert Loan_Amount_Term which is in months to a year and store the result in a variable 'loan_term' 

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )

# Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 'big_loan_term'

big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)
# code ends here

print('='*50)
# step 6
# code starts here


# Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History'] and store the subsetted dataframe back in 'loan_groupby'

loan_groupby=banks.groupby(['Loan_Status'])
# Groupby the 'banks' dataframe by Loan_Status and store the result in a variable called 'loan_groupby'

loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']] 


# Check the mean value of 'loan_groupby'
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here



