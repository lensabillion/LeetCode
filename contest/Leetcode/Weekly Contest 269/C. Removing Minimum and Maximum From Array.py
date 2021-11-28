class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        _min = float('inf')
        _max = float('-inf')
        hash_map = {}
        for i in range(len(nums)):
           
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            if nums[i] > _max:
                _max = nums[i]
            if nums[i] < _min:
                _min = nums[i]
        
        ind_min = hash_map[_min]
        ind_max = hash_map[_max]
        if len(nums) <= 2:
            return len(nums)
        front_min = (ind_min + 1) - 0
        back_min  =  (len(nums) - ind_min)
        front_max = (ind_max + 1) - 0
        back_max  =  (len(nums) - ind_max)
       
        return min(max(front_min, front_max ), max(back_min, back_max), min(front_min, back_min) + min(front_max, back_max))
        