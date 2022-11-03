class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''  # Store the longest substring
        ret = ''  # Store the current substring without repeating
        for c in s:
            if c in ret:
                ret = ret[ret.find(c)+1:]  # Truncat the current substring by the position of repeating character
            ret += c  # Append character doesn't repeat in substring 
            longest = ret if len(ret) > len(longest) else longest  # Replace longest substring if current substring is longer

        return len(longest)    