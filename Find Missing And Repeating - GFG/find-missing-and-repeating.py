#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        d= {}
        for i in range(1,n+1):
            d[i] = 0
            
        for i in arr:
            d[i]+=1
            
        def getkey(value):
            for k,v in d.items():
                if v == value:
                    return k
                    
        return getkey(2),getkey(0)
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends