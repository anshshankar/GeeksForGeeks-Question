#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        mini = A[M-1]-A[0]
        for i in range(1,N-M+1):
            mini = min(mini,A[M+i-1]-A[i])
        return mini

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends