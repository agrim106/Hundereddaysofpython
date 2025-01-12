# Problem 2: Group Anagrams
# Given an array of strings strs, group the anagrams together.
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        sorted_str = ''.join(sorted(s))
        anagram_groups[sorted_str].append(s)
        
    return list(anagram_groups.values())

# Test cases
assert sorted(group_anagrams(["eat","tea","tan","ate","nat","bat"])) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]