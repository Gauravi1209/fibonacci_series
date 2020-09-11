n = int(input("Enter the range of numbers:"))
num = 0
a = 0
b = 1
count = 0

while (count<n):
    print(a,end=', ')
    num = a + b
    a = b
    b = num
    count +=1
