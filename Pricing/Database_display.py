import pandas as pd

row = int(input("which row?"))

df = pd.read_csv (r"C:\Users\aadit\Documents\Python\.vscode\AP CSP Create Task\AP-CSP-Create-Task\Pricing\Datasets\Public_Garages_or_Parking_Lots - Public_Garages_or_Parking_Lots.csv")

print (df)
print(df.iloc[row,0:2])
