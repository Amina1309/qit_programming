# 3. Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(self, s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
        
    Args:
        s (str): Input string
            
    Returns:
        int: Length of the longest substring without repeating characters
    """
    substring = {}
    max_length = 0
    start = 0
        
    for end, char in enumerate(s):
        if char in substring:
            start = max(start, substring[char] + 1)
        substring[char] = end
        max_length = max(max_length, end - start + 1)
        
    return max_length