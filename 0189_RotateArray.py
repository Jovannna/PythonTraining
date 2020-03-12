class Solution(object):
    def rotate(self, nums, k):
        kLenArr=[None]*(len(nums)-k)
        for i in range(len(nums)-k,len(nums)):
            kLenArr[i-k]=nums[i]
        i=len(nums)-1
        while i>=k:
            nums[i]=nums[i-k]
            i-=1
        for i in range(0,k):    
            nums[i]=kLenArr[i-k]
        return nums

def test(inputList, k, outputList):
    """ Internal test function, with output to console """

    # Copy initial input list by value, not as reference. We need this only to print data to console in case of a wrong solution.
    inputListCopy = inputList[:]

    sol = Solution()
    sol.rotate(inputList, k)

    n = len(inputList)
    solOK = True
    for index in range(n):
        if (inputList[index] != outputList[index]):
            solOK = False
            break

    if (solOK):
        print('{0} - input = {1}'.format(solOK, inputListCopy))
    else:
        print('{0} - input = {1}, output = {2}, expected = {3}'.format(solOK, inputListCopy, inputList, outputList))

test([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])
test([1,2,3,4,5,6,7,8],4,[5,6,7,8,1,2,3,4])