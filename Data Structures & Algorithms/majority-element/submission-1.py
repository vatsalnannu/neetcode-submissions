class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hmap = {}
        # for i in nums:
        #     if i in hmap:
        #         hmap[i]+=1
        #     else:
        #         hmap[i]=1

        # for i in hmap.keys():
        #     if hmap[i]>len(nums)//2:
        #         return i

        count= 1
        res = nums[0]

        for i in range(1,len(nums)):
            if count==0 and nums[i]!=res:
                res = nums[i]
            if nums[i] == res:
                count+=1
            else:
                count-=1
        return res
            