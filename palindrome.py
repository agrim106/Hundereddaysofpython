# Problem 1: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
def longest_palindromic_substring(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if not s:
        return ""
        
    longest = s[0]
    for i in range(len(s) - 1):
        # Odd length palindromes
        palindrome1 = expand_around_center(i, i)
        # Even length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
            
    return longest

# Test cases
assert longest_palindromic_substring("babad") == "bab"  # or "aba"
assert longest_palindromic_substring("cbbd") == "bb"
assert longest_palindromic_substring("a") == "a"