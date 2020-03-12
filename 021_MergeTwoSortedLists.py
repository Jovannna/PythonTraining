class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def listToArray(self):
        arr=[]
        l = self
        while l!=None:
            arr.append(l.val)
            l=l.next
        return arr


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        last=None
        lresult=None
        while (l1!=None) and (l2!=None):
            if l1.val<=l2.val:
                if lresult==None:
                    lresult=l1
                else: 
                    last.next=l1
                last=l1
                l1=l1.next
                
            else:
                if (l2.val<l1.val):
                    if lresult==None:
                        lresult=l2   
                    else: 
                        last.next=l2 
                    last=l2 
                l2=l2.next
                       
        if (l1==None):
            last.next=l2
        else:
            last.next=l1
        return lresult
            
def arrayToList(arr):
    l=None
    for i in range(len(arr)):
        if l==None:
            l=ListNode(arr[i])
            last=l
        else:
            pom=ListNode(arr[i])
            last.next=pom
            last=last.next
    return l

def test(resultList, inputList2, outputList):
    
    sol = Solution()
    list1=arrayToList(inputList1)
    
    list2=arrayToList(inputList2)
    
    list3=sol.mergeTwoLists(list1,list2)

    resultList=list3.listToArray()

    n = len(inputList)
    solOK = True
    for index in range(n):
        if (inputList[index] != outputList[index]):
            solOK = False
            break

    if (solOK):
        print('{0} - input = {1}, {2}'.format(solOK, inputList1, inputList2))
    else:
        print('{0} - input = {1}, {2}, output = {3}, expected = {4}'.format(solOK, inputList1, inputList2, resultList, outputList))

test([1,2,4],[1,3,4], [1,1,2,3,4,4])
