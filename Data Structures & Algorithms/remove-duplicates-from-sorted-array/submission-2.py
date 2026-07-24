class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = sorted(set(nums))
        nums[:len(uniq)] = uniq
        return len(uniq )