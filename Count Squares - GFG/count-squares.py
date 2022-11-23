#User function Template for python3

class Solution:
    def countSquares(self, N):
        # code here 
        sn = math.sqrt(N)
        if sn==int(sn):
            return int(sn-1)
        else:
            return int(sn)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends