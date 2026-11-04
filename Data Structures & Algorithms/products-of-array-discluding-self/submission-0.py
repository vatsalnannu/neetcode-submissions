class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        res=[]
        for i in range(len(nums)):
            prod*=nums[i]
            res.append(prod)
        prefix = res
        prod=1
        res1 = []
        for i in range(len(nums)-1,-1,-1):
            prod*=nums[i]
            res1.append(prod)
        postfix = res1[::-1]
        final = []
        for i in range(len(nums)):
            if i==0:
                final.append(1*postfix[i+1])
            elif i==len(nums)-1:
                final.append(prefix[i-1]*1)
            else:
                final.append(prefix[i-1]*postfix[i+1])
        return final
