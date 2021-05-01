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


#define Div_Num function
def div_num(y):
    return x/y

#div by values num_list
map_output = map(div_num, num_list)
output_list = list(map_output)
print(output_list)

#round up values for output_list
round_list = [round(num) for num in output_list]
print(round_list)

#divide rounded by output
div_output = [i / j for i, j in zip(round_list, output_list)]
print(div_output)

#count instances of 1 in div_output
output_occur = div_output.count(1.0)
print(output_occur)

#if argument detects if list has 1 or not
if output_occur == 0:
    print("prime")
else:
    print("composite")