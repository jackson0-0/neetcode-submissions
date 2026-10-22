class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        #memory 
        numSet = set(nums)
        longest = 0 

        for num in numSet: 
            #checking 
            if (num-1) not in numSet:
                length = 1 
                while num + length in numSet:
                    length += 1 
                #record 
                longest = max(length, longest) 
        #return 
        return longest 