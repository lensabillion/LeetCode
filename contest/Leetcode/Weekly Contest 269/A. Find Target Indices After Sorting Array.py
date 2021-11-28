class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        O(nlog(n))
        n = sorted(nums)
        ans = []
        for i in range(len(n)):
            if n[i] == target:
                ans.append(i)
        return ans
        """
        # O(N)
        cnt_smaller = 0
        cnt_equal = 0
        for i in nums:
            if i < target:
                cnt_smaller += 1
            if i == target:
                cnt_equal += 1
        return range(cnt_smaller, cnt_smaller + cnt_equal)