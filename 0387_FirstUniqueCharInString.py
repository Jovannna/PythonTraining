class Solution(object):
    def firstUniqeChar(self, s):
        dict={}
        uniqueEl=' '
        indexOfUnique=-1
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1   
            else:
                dict[s[i]]=1
        for x in dict:
            if dict[x]==1:
                uniqueEl=x
                break;
        if uniqueEl!=' ':
            i=0;
            while i<len(s):
                if s[i]==uniqueEl:
                    indexOfUnique=i
                    break;
                i+=1
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
test("aab",2)