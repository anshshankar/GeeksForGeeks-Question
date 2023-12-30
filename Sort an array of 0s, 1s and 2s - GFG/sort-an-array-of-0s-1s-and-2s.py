#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        o,t,z = 0,0,0
        for i in arr:
            if i==0:
                z+=1
            elif i==1:
                o+=1
            else:
                t+=1
        arr[:z] = [0]*z
        arr[z:z+o] = [1]*o
        arr[z+o:] = [2]*t
        return arr
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends