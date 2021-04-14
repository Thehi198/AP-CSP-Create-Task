#input
x = int(input("which number?"))
x = abs(x)
print(x)

array = [1,2,5,7]
if x in array:
    print("prime")
    quit

#initialize
a = x
b = x
c = x
d = x
r = 0

# div 2?
while a > 0:
    a = a - 2
print (a)
if a == 0:
    print("div 2; composite")
    SystemExit
else:
    print("not 2")

# div 3?
while b > 0:
    b = b - 3
print (b)
if b == 0:
    print("div 3; composite")
    SystemExit
else:
    print("not 3")

# div 5?
while c > 0:
    c = c - 5
print (c)
if c == 0:
    print("div 5; composite")
    SystemExit
else:
    print("not 5")


# div 7?
while d > 0:
    d = d - 7
print (d)
if d == 0:
    print("div 7; composite")
    SystemExit
else:
    print("not 7")


