numbers = [10, 20, 30, 40, 50]
n = int(input("Enter the number to search: "))

for i in range(len(numbers)):
    if numbers[i] == n:
        print(i) 
        break
else:
    print("Number is not found in the list")
   
