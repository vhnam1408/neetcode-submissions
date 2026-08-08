from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Sắp xếp mảng theo chiều dài của các từ tăng dần
        words.sort(key=len)
        res = []
        
        # Duyệt qua từng từ trong mảng
        for i in range(len(words)):
            # Chỉ cần so sánh với các từ đứng sau (dài hơn hoặc bằng)
            for j in range(i + 1, len(words)):
                # Nếu từ hiện tại là chuỗi con của một từ dài hơn
                if words[i] in words[j]:
                    res.append(words[i])
                    # Đã xác định được nó là chuỗi con, dừng kiểm tra để tránh trùng lặp
                    break
                    
        return res