class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = { }
        res = 0
        left = 0
        max_f = 0
        for right in range(len(s)): 
            cnt[s[right]] = 1 + cnt.get(s[right], 0)
            max_f = max(max_f, cnt[s[right]])
            while(right - left + 1)- max_f > k: 
                cnt[s[left]]-= 1
                left+= 1

            res  =max(res, right- left + 1) 
        return res;