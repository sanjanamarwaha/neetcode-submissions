class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        # [17,18,5,4,6,1]
        n = len(arr) #n = 6
        ans = [0] * n   #[0,0,0,0,0,0]
        rightMax = -1
        for i in range(n-1, -1, -1):
            ans[i] = rightMax   #[0,0,0,0,0,-1]
            rightMax=max(arr[i], rightMax) #-1
        return ans
        