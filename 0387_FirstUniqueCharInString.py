class Solution(object):
    def firstUniqeChar(self, s):
        a={s[len(s)-1]}
        indexOfUnique=len(s)-1
        i=len(s)-2
        uniqueEl=s[len(s)-1]
        while i>=0:
            if s[i] in a:
                if s[i]==uniqueEL:
                    indexOfUnique=-1   
            else:
                a.add(s[i])
                indexOfUnique=i
                uniqueEL=s[i]
            i-=1
        return indexOfUnique

def test(inputString, outputInt):
    sol=Solution()
    out=sol.firstUniqeChar(inputString)
 
    solOK = True
    if (out!= outputInt):
        solOK = False

    if solOK:
        print('{0} - input = {1}'.format(solOK, inputString))
    else:
        print('{0} - input = {1}, output = {2}, expected = {3}'.format(solOK, inputString, out, outputInt))

test("leetcode",0)
test("loveleetcode",2)