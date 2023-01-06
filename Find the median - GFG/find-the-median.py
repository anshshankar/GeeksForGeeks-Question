#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		n = len(v)
		if n%2==0:
		    m1 = n//2
		    m2 = m1-1
		    m1 = v[m1]
		    m2 = v[m2]
		    m = (m1+m2)//2
		    
	    else:
	        m = n//2
	        m = v[m]
	        
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends