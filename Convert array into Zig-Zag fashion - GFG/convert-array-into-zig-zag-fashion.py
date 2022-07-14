#User function Template for python3
class Solution:
	def zigZag(self,arr, n):
	    for i in range(0,n-1,2):
	        if(arr[i]>arr[i+1]):
	            arr[i],arr[i+1]=arr[i+1],arr[i]
	        if(i!=(n-2) and arr[i+1]<arr[i+2]):
	            arr[i+1],arr[i+2]=arr[i+2],arr[i+1]
	       # i+=1
	  
	  
	  
	  
	  
	  
	  
	  
	  
	   # i=0
	   # j=0
	    
# 		while(i<n-1):
# 		    if(arr[i]>arr[i+1] and j%2==0):
# 		        arr[i],arr[i+1] = arr[i+1],arr[i]
# 		        j+=1
# 		  #  print(arr)
		        
# 		    if(arr[i]<arr[i+1]):
# 		        arr[i-1],arr[i] = arr[i],arr[i-1]
# 		        j+=1
# 		    i+=1
# 	    return arr
		    
		
		        
		    
		    
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends