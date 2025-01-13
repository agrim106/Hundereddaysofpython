# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if string is palindrome
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# 3. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = sum(1 for c in s.lower() if c in 'aeiou')
    consonants = sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')
    return vowels, consonants

# 4. Remove duplicates from string
def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))

# 5. Find all substrings of a string
def find_all_substrings(s):
    substrings = [s[i:j] for i in range(len(s)) 
                 for j in range(i + 1, len(s) + 1)]
    return substrings

# 6. Check if strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Test the functions
def test_string_functions():
    # Test reverse string
    print("1. Reverse string:")
    test_str = "Hello, World!"
    print(f"Original: {test_str}")
    print(f"Reversed: {reverse_string(test_str)}")
    
    # Test palindrome
    print("\n2. Palindrome check:")
    test_palindrome = "A man, a plan, a canal: Panama"
    print(f"Is '{test_palindrome}' a palindrome? {is_palindrome(test_palindrome)}")
    
    # Test vowel and consonant count
    print("\n3. Count vowels and consonants:")
    test_count = "Hello World"
    vowels, consonants = count_vowels_consonants(test_count)
    print(f"In '{test_count}':")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    
    # Test remove duplicates
    print("\n4. Remove duplicates:")
    test_dup = "programming"
    print(f"Original: {test_dup}")
    print(f"Without duplicates: {remove_duplicates(test_dup)}")
    
    # Test find substrings
    print("\n5. Find substrings:")
    test_sub = "abc"
    print(f"All substrings of '{test_sub}': {find_all_substrings(test_sub)}")
    
    # Test anagrams
    print("\n6. Check anagrams:")
    str1, str2 = "Silent", "Listen"
    print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")

if __name__ == "__main__":
    test_string_functions()