#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        i,j = 0,0
        curr = 0
        if s==0:
            return [-1]
       
        while j<len(arr) or curr>=s:
            if curr==s:
                return [i+1,j]
            elif curr<s:
                curr+=arr[j]
                j+=1
                # print(curr,"hello")
            else:
                curr-=arr[i]
                i+=1
                # print(curr,"world")
        return [-1]
              
               
           
       
       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends