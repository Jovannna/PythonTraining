class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
  

class Solution(object):
    def maxDepth(self, root):
        currMaxDepth = 0
        if root != None:
            maxDepthLeft=self.maxDepth(root.left)
            maxDepthRight=self.maxDepth(root.right)
            if (maxDepthLeft>maxDepthRight):
                currMaxDepth = maxDepthLeft+1
            else:
                currMaxDepth = maxDepthRight+1
        return currMaxDepth


def arrayToTree(arr, i):
    if i<len(arr):
        if (arr[i]!=None):
            root = TreeNode(arr[i])
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
test([1,2,3,4,5,None,None,6,7],4)