string = ["4","-","4","-","3","-","1","-","2","-","5","-"]
nums = {"1","2","3","4","6","7","8","9"}
for num in string:
    if num in nums:
        nums.remove(num)
print(nums[0])