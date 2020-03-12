class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        currMaxDepth = 0
        currRoot = root
        if currRoot != None:
            if (self.maxDepth(root.left)>self.maxDepth(root.right)):
                currMaxDepth = self.maxDepth(root.left)+1
            else:
                currMaxDepth = self.maxDepth(root.right)+1
        return currMaxDepth


def arrayToTree(arr, i):

    if i<len(arr):
        if (arr[i]!=None):
            temp = TreeNode(arr[i])
            root = temp
            root.left = arrayToTree(arr,2*i+1)	
            root.right = arrayToTree(arr,2*i+2)
            return(root)    
    return None
            
def test(inputArray, outputInt):
    sol = Solution()

    inputRoot = arrayToTree(inputArray,0)
    out = sol.maxDepth(inputRoot)
    

    solOK = True
    if (out!= outputInt):
        solOK = False

    if solOK:
        print('{0} - input = {1}'.format(solOK, inputArray))
    else:
        print('{0} - input = {1}, output = {2}, expected = {3}'.format(solOK, inputArray, out, outputInt))


test([3,9,20,None,None,15,7],3)