def prime_function(input):
    n = input/2
    n = int(n)
    num_range = range(2,n)
    num_list = list(num_range)
    def div_num(y):
        return input/y
    map_output = map(div_num, num_list)
    output_list = list(map_output)
    round_list = [round(num) for num in output_list]
    div_output = [i / j for i, j in zip(round_list, output_list)]
    output_occur = div_output.count(1.0)
    if output_occur == 0:
        print(input, "is prime")
    else:
        print(input, "is composite")
def input_function():
    print("Enter numbers to calculate. Please seperate values by hiitting enter. Press enter twice or type stop once you are done")
input_function()
try:
    input_list = []
      
    while True:
        input_list.append(int(input()))
except:
    print(input_list)
output_array = map(prime_function, input_list)
output_list = list(output_array)