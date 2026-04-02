class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_num = 0
        count = {}
        filtered_nums = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for number, counts in count.items():
            if counts == 1:
                filtered_nums.append(number)
        if not filtered_nums :
            return -1   
        else:
            for num in filtered_nums:
                max_num = max(max_num, num)
            return max_num
