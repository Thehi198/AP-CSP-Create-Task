#input and processing
x = input("which number?")
x = int(x)
x = abs(x)
print(x)

#div value
n = x/2
n = int(n)
print(n)

#find values between 2,n
num_range = range(2,n)
num_list = list(num_range)
print("list of numbers between 2 and N:" , num_list)

#count number of elements in list
num_elem = len(num_list)
print("Number of elements in num_list:" ,num_elem)

#define Div_Num function
def div_num(y):
    return x/y

#div by values num_list
map_output = map(div_num, num_list)
output_list = list(map_output)
print(output_list)

