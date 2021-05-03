x = input ("array")
print(x)
list(x)

#define Div_Num function
def div_num(y):
    return input/y

#div by values num_list
map_output = map(div_num, x)
output_list = list(map_output)
print(output_list)
