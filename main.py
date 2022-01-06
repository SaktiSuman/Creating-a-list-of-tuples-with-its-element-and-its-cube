count = int(input("Enter the number of elements in the list: "))
l = []
for i in range(count):
    x = int(input("Enter the element: "))
    l.append(x)
res = [(val, pow(val, 3)) for val in l]
print(res)