class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1

        for i in hmap.keys():
            if hmap[i]>len(nums)//2:
                return i