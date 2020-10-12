import gspread
import matplotlib.pyplot as plt
import pandas as pd

# paste your credentails file name in service account filename
gc = gspread.service_account(filename='credentials.json')

# paste your Google Sheet Link in open_by_url 
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/133jnnPzkSmrYEGfNbWaUbzJIRLhUepzM4TlB08HR-cA/edit#gid=0')
worksheet = sh.sheet1

# Please Enter Your Valid X--Axis 
row_name = worksheet.row_values(1)
print('Enter Your X Axis From The List of Columns\n')
print(row_name,'\n')
print('1 For Frist Column 2 For Second Column And So On .......\n')
X=int(input())

# Please Enter Your Valid Y--Axis
print('Enter Your Y Axis From The List of Columns\n')
print(row_name,'\n')
print('1 For Frist Column 2 For Second Column And So On .......\n')
Y=int(input())

# This line handling that user is giving right X and Y Axis or Not 

if X<=len(row_name) and Y<=len(row_name):

    # Getting All Columns After 1st Row For X--Axis
    
    X_values_list = worksheet.col_values(X)
    values_of_X=[]
    for i in X_values_list[1:]:
        values_of_X.append(int(i))

    print('Values On X Axis:- ',values_of_X)

    # Getting All Columns After 1st Row For Y--Axis
    
    Y_values_list = worksheet.col_values(Y)
    values_of_Y=[]
    for i in Y_values_list[1:]:
        values_of_Y.append(int(i))
    print('\nValues On Y Axis:- ',values_of_Y)
    
    # Here We are going to plot the Graph of data with X and Y Axis
    plt.plot(sorted(X_values_list),sorted(Y_values_list)) 
    plt.xlabel(row_name[X-1]+' - Axis') 
    plt.ylabel(row_name[Y-1]+' - Axis') 
    plt.title('Assignment of Greendeck') 
    plt.show()

else:
    print('Please Enter a Valid Number and Run Again')
