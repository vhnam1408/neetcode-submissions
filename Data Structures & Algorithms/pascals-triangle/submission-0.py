from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        # Xây dựng từng hàng từ trên xuống dưới
        for i in range(numRows):
            # Khởi tạo một hàng mới chứa toàn số 1, có kích thước i + 1
            row = [1] * (i + 1)
            
            # Tính toán các giá trị nằm ở giữa hàng (bỏ qua số 1 ở đầu và cuối)
            for j in range(1, i):
                # Mỗi phần tử bằng tổng của 2 phần tử ngay phía trên nó
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
                
            # Thêm hàng vừa tạo vào kết quả
            res.append(row)
            
        return res