#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        l = list(S)
        li = list(l[0])
        j = 0
        for i in l:
            if i == li[j]:
                continue
            li.append(i)
            j+=1
        return "".join(li)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends