nums = [1, 2, 3, 4, 5]
target = 9

# Finding the two values
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Values are:", nums[i], "and", nums[j])

