#define function for counting number of intigers in list
type_output = 0
def checkType(output_list):
    for element in output_list:
        if isinstance(element, int):
            type_output = type_output + 1
print(type_output)