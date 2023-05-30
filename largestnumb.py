class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(number) for number in nums]
        def compare(x,y):
            return int(y+x) - int(x+y)
        
        nums.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums)
        
        if largest_num[0] == '0':
            return '0'
        
        return largest_num