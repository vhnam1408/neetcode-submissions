from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Bước quan trọng để gom các phần tử trùng lặp lại với nhau
        nums.sort()
        
        def back_track(i, subset):
            # Nếu đã duyệt qua hết mảng, lưu kết quả
            if i == len(nums):
                res.append(subset[::])
                return
            
            # Lựa chọn 1: BAO GỒM phần tử nums[i]
            subset.append(nums[i])
            back_track(i + 1, subset)
            
            # Xóa phần tử vừa thêm để quay lui (chuẩn bị cho Lựa chọn 2)
            subset.pop()
            
            # Lựa chọn 2: KHÔNG BAO GỒM phần tử nums[i]
            # Để tránh trùng lặp, ta phải bỏ qua tất cả các số giống hệt nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            # Lời gọi đệ quy này PHẢI NẰM NGOÀI vòng while
            back_track(i + 1, subset)
            
        back_track(0, [])
        return res