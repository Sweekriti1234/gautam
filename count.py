'''a = [2,7,9,8,5]
count = 0
for ele in a:
    if ele % 2 ==0:
        count += 1
print(count)'''
nums = [3, 4, 6, 9, 10]
'''nums1 = nums[0:4]
def array_front9(nums1):
    for ele in nums1:
        if ele % 9 == 0:
            print("True")
        else:
            print("False")
array_front9(nums1)'''

flag = False
nums = nums[0:4]
def array(nums):
    
    flag = False
    if 9 in nums:
        flag = True
    return flag

print(array(nums))
