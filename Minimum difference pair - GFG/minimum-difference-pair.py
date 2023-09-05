#User function Template for python3

class Solution:
	def minimum_difference(self, nums):
		# Code here
		nums.sort()
		m = 10e9
		for i in range(1,len(nums)):
		    m = min(m,nums[i]-nums[i-1])
		return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.minimum_difference(nums)
		print(ans)
# } Driver Code Ends