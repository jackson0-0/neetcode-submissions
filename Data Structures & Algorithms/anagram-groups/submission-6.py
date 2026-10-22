class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #hashtable , then map all the base map to keys, then map the different words in a list inside the values of the key 
        result = defaultdict(list)
        for string in strs: 
            count = [0] * 26 
            for char in string:
                 count[ord(char)-ord('a')] +=1
            result[tuple(count)].append(s)
        return list(result.values())
        