str = "civic"
reverse_str=""

for ch in str:
  reverse_str = ch + reverse_str
  
print(str)
print(reverse_str)

if str==reverse_str:
    print("Palindrome")
else:
    print("Not a palindrome")
