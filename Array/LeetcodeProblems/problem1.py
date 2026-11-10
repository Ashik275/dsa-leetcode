# from array import *

# arr = [2,7,11,15];
# n= len(arr)
# target = 9;
# for i in range(n):
#     for j in range (i+1,n):
#         if arr[i]+arr[j] == target:
#             print(i,j)

class Solution:
    def twoSum(self,nums,target):
        mydict ={}

        for i in range(len(nums)):
            if target-nums[i]  in mydict:
                return (i,mydict[target-nums[i]])

            mydict[nums[i]]= i

rel =Solution()

a=rel.twoSum([2,7,11,15],9)
print(a);


        

