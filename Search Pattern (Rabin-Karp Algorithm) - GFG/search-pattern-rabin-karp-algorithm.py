#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        res = []
        p = len(patt)
        a = ""
        for i in range(len(s)-p+1):
            a = s[i:i+p]
            if s[i:i+p] == patt:
                res.append(i+1)
        # print(a)
        if res==[]:
            return [-1]
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends