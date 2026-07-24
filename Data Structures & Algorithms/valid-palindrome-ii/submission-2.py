class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Nếu khác nhau, thử xóa s[l] hoặc s[r]
                # Lấy chuỗi con sau khi xóa l: s[l+1 : r+1]
                # Lấy chuỗi con sau khi xóa r: s[l : r]
                skip_l = s[l+1 : r+1]
                skip_r = s[l : r]
                
                # Trả về True nếu một trong hai chuỗi con là đối xứng
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            
            # Cập nhật con trỏ nếu hai ký tự giống nhau
            l += 1
            r -= 1
            
        return True