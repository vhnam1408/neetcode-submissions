class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        ans = nums[0]
        while( l <= r) : 
            mid = ( l + r ) //2 
            if nums[mid] >= nums[0]:
                l = mid + 1
            else: 
                ans = nums[mid]
                r = mid - 1
        return ans