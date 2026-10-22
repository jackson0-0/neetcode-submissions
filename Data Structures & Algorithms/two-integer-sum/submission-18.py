class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #memory : dict 
        seen = {}
        for index, value in enumerate(nums):
            #check
            diff = target - value
            if diff in seen:
                return [seen[diff], index]
            #record
            seen[value] = inde
        #result
        return None