class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        # Duyệt cho đến khi 1 trong 2 con trỏ đi hết chuỗi tương ứng
        while i < len(s) and j < len(t):
            # Nếu ký tự khớp, di chuyển con trỏ của chuỗi s
            if s[i] == t[j]:
                i += 1
            # Luôn luôn di chuyển con trỏ của chuỗi t
            j += 1
            
        # Nếu i duyệt hết chuỗi s, tức là s là chuỗi con của t
        return i == len(s)