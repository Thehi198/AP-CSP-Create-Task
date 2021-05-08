def prime_function(input):

    #input Processing
    input = int(input)
    input = abs(input)

    #div value
    n = input/2
    n = int(n)

    #find values between 2,n
    num_range = range(2,n)
    num_list = list(num_range)

    #define Div_Num function
    def div_num(y):
        return input/y

    #div by values num_list
    map_output = map(div_num, num_list)
    output_list = list(map_output)

    #round up values for output_list
    round_list = [round(num) for num in output_list]

    #divide rounded by output
    div_output = [i / j for i, j in zip(round_list, output_list)]

    #count instances of 1 in div_output
    output_occur = div_output.count(1.0)

    #if argument detects if list has 1 or not
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