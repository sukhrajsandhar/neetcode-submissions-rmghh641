class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        prev_num = 0
        for num in nums:
            if num == prev_num:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0 
                prev_num = num
        return max_streak + 1