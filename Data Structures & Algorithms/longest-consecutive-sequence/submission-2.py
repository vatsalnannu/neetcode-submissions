class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        arr = []
        for i in num_set:
            if i - 1 not in num_set:
                arr.append(i)

        max_count = 0
        for i in arr:
            j = i
            count = 0
            while j in num_set:
                count += 1
                j += 1
            max_count = max(max_count, count)
        return max_count