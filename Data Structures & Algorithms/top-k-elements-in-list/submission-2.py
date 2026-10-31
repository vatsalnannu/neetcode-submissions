class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hmap = {}
        # i=0
        # current_i = 0
        # while i < len(nums):
        #     count=0
        #     while current_i < len(nums) and nums[i]==nums[current_i]:
        #         count+=1
        #         current_i+=1
        #     if nums[i] in hmap.keys():
        #         hmap[nums[i]] = max(hmap[nums[i]],count)
        #     else:
        #         hmap[nums[i]] = count
        #         i=current_i
        
        # return sorted(hmap, key=hmap.get, reverse=True)[:k]
        hmap = {}
        for i in nums:
            if i in hmap.keys():
                hmap[i]+=1
            else:
                hmap[i]=1
        return sorted(hmap, key=hmap.get, reverse=True)[:k]
