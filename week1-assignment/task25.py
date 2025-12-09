n = int(input("Enter the number for fibonacci series: "))

num1 = 0
num2 = 1

for i in range(n) :
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3

