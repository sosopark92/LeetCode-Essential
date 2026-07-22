# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            anagram_map[sorted_key] = anagram_map.get(sorted_key, []) + [s]
        return list(anagram_map.values())
    

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted words to their original anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort characters to create a unique key
            sorted_key = "".join(sorted(s))
            # Append original word to the list
            anagram_map[sorted_key].append(s)
            
        # Return grouped lists
        return list(anagram_map.values())