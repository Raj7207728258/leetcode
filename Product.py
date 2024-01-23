class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        m = len(nums)
        l_products = [1] * m
        r_products = [1] * m
        l_product = 1
        for i in range(1, m):
            l_product *= nums[i - 1]
            l_products[i] = l_product
        r_product = 1
        for i in range(m - 2, -1, -1):
            r_product *= nums[i + 1]
            r_products[i] = r_product
        result = [1]*m
        for i in range(m):
            result[i] = l_products[i]*r_products[i]    
        return result