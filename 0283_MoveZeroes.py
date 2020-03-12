class Solution(object):
    def moveZeroes(self, nums):
        numOfZeroes=0
        for i in range(len(nums)):
            if nums[i]==0:
                numOfZeroes+=1
            else:
                if numOfZeroes>0:
                    nums[i-numOfZeroes]=nums[i]
                    nums[i]=0
        

def test(inputList, outputList):
    inputListCopy = inputList[:]

    sol = Solution()
    sol.moveZeroes(inputList)

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

test([0, 1, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0])
test([1, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0])
test([1, 2, 0, 0, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0, 0])
test([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0,0,0])

                