class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        prefix = [0] * (len(nums))
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        d = 2*k + 1   
        for i in range(k, len(nums)-k):
            
            c = ( i-k) - 1
          
            if c >= 0:
                
                avg = (prefix[i+k] - prefix[c]) // d
            else:
                avg = (prefix[i+k]) // d
            ans[i] = avg
        return ans