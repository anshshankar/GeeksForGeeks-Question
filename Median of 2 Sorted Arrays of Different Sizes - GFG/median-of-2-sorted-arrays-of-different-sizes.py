#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            array1.extend(array2)
            array1.sort()
            l = len(array1)
            if l%2 == 0:
                m1 = (l//2)
                m2 = (l//2)-1
                m1,m2 = array1[m1], array1[m2]
                m = (m1+m2)/2
                if m == int(m):
                    return int(m)
                return m
            else:
                m = l//2
                return array1[m]
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends