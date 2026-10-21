class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set=[]
        for i in nums:
            if i in check_set:
                return True
            else:
                check_set.append(i)
        return False