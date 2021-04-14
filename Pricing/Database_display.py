import pandas as pd

data = pd.read_csv (r"C:\Users\aadit\Documents\Python\.vscode\AP CSP Create Task\AP-CSP-Create-Task\Pricing\Datasets\Public_Garages_or_Parking_Lots - Public_Garages_or_Parking_Lots.csv")
df = pd.DataFrame(data, columns= ["x","y"])
print (df) 
