class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_num = 0

        for num in nums:
            if num == prev_num:
                return True 
            else:
                prev_num = num
        else:
            return False