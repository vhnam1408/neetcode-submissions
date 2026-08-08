class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score = 0
        
        # Duyệt qua từng cặp ký tự liền kề
        for i in range(len(s) - 1):
            # Tính khoảng cách ASCII tuyệt đối và cộng dồn
            total_score += abs(ord(s[i]) - ord(s[i+1]))
            
        return total_score