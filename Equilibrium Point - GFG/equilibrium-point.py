# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        larr=0
        rarr=sum(A)-A[0]
        
        if(len(A)==1):
            return 1
        
        for i in range(0,N-1):
            if(larr==rarr):
                return i+1
            
            larr+=A[i]
            rarr-=A[i+1]
            
        return -1
                
        
        
        


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends