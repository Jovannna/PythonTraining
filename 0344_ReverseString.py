from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """ Method for reversing input string list, inline """
        sLen = len(s)
        for index in range(sLen//2):
            tmpValue = s[index]
            s[index] = s[sLen - index - 1]
            s[sLen - index - 1] = tmpValue

def test(inputList, outputList):
    """ Internal test function, with output to console """

    # Copy initial input list by value, not as reference. We need this only to print data to console in case of a wrong solution.
    inputListCopy = inputList[:]

    sol = Solution()
    sol.reverseString(inputList)

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

test(["h","e","l","l","o"], ["o","l","l","e","h"])
test(["H","a","n","n","a","h"], ["h","a","n","n","a","H1"])
test(["a"], ["a"])
test(["a", "b"], ["b", "a"])
test([], [])