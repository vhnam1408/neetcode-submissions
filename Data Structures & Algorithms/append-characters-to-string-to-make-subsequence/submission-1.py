class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        
        # Duyệt qua các ký tự của s và t
        while i < len(s) and j < len(t):
            # Nếu tìm thấy ký tự khớp, chuyển sang tìm ký tự tiếp theo của t
            if s[i] == t[j]:
                j += 1
            # Luôn di chuyển con trỏ i để duyệt tiếp chuỗi s
            i += 1
            
        # Số ký tự cần thêm chính là phần còn lại của chuỗi t chưa được khớp
        return len(t) - j