# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    for i in arr:
        l=int(i)
        i=int(i)
        s=0
        while(i>0):
            d=i%10
            i=i//10
            s=s*10+d
            
            
        if(l==s):
            continue
        
        else:
            return 0
            
    return 1
            



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends