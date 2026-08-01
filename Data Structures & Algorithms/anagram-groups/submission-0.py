from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        # count = 0
        hashmap = defaultdict(list) # key: sorted(word) , values: word
        result =[]

        for word in strs:
            sort_word = tuple(sorted(word))
            hashmap[sort_word].append(word)
        
        for value in hashmap.values():
            result.append(value)

        return result

            



      
