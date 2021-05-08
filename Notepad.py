def variance(data):
    # Number of observations
    n = len(data)
    # Mean of the data
    mean = sum(data) / n
    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]
    # Variance
    variance = sum(deviations) / n
    return variance
...
print("Enter numbers to calculate. Please seperate values by hiitting enter. Press enter twice or type stop once you are done")
try:
    input_list = []
      
    while True:
        input_list.append(int(input()))
except:
    print(input_list)

list(input_list)
print(input_list)

output_array = map(variance, input_list)
output_list = list(output_array)