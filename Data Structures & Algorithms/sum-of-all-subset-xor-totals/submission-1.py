
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def back_track(i, subset): 
            nonlocal res
            xorr = 0
            for num in subset: 
                xorr ^= num
            res += xorr
            for j in range(i, len(nums)): 
                subset.append(nums[j])
                back_track(j+1, subset)
                subset.pop()
        back_track(0,[ ]) 
        return res