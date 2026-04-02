class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_value = 0
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count.values():
            max_value = max(max_value, num)
        
        for key, num in count.items():
            if num == max_value:
                return key
                break
        