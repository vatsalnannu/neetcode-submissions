class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i=0
        # j=0
        # count=0
        # while i<len(nums) and j<len(nums):
        #     if nums[j]==val:
        #         nums[j]='_'
        #     else:
        #         nums[i] = nums[j]
        #         i+=1
        #         j+=1
        # for i in nums:
        #     if i=='_':
        #         continue
        #     else:
        #         count+=1
        # return count
        k=0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        
        return k
