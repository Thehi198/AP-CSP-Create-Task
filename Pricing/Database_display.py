import pandas as pd

row = int(input("which row?"))

df = pd.read_csv (r"C:\Users\aadit\Documents\Python\.vscode\AP CSP Create Task\AP-CSP-Create-Task\Pricing\Datasets\Public_Garages_or_Parking_Lots - Public_Garages_or_Parking_Lots.csv")

print (df)
print(df.iloc[row,0:2])

#find garage name in file
    #find garage name in collumn 4
#find based on GPS location relitive to C3,4
    #find nearest location to user

