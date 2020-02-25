class Solution(object):
    def moveZeroes(self, nums):
        nonzeroi=len(nums)-1
        i=0
        while i<nonzeroi:
            if nums[i]!=0:
                i+=1
            else:
                for j in range(i,nonzeroi):
                    nums[j]=nums[j+1]
                nums[nonzeroi]=0
                nonzeroi-=1

sol=Solution()
print('Enter the array:')
a=[int(x) for x in input().split()]
sol.moveZeroes(a)
print(a)
                