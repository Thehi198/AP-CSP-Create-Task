#input
x = input("which number?")
x = int(x)
x = abs(x)
print(x)

array = [1,2,5,7]
if x in array:
    print("prime")
    SystemExit

#initialize
a = x
b = x
c = x
d = x
r = 0

# div 2?
d = d % 2
print (d)
if d == 0:
    print("div 2; composite")
    SystemExit
else:
    print("not 2")

# div 3?
d = d % 3
print (d)
if d == 0:
    print("div 3; composite")
    SystemExit
else:
    print("not 3")

# div 5?
d = d % 5
print (d)
if d == 0:
    print("div 5; composite")
    SystemExit
else:
    print("not 5")


# div 7?

d = d % 7
print (d)
if d == 0:
    print("div 7; composite")
    SystemExit
else:
    print("not 7")

#div x half number and div x uptil number 