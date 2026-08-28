class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zero = 0
        for x in nums:
            if x != 0:
                product *= x
            else:
                zero += 1
        for x in nums:
            if zero > 1 or x != 0 and zero == 1:
                output.append(0)
            elif x == 0:
                output.append(product)
            else:
                output.append(product//x)


        return output