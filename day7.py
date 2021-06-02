Link:https://leetcode.com/problems/valid-parentheses/

"""

💻 List of Companies: Amazo, Apple, Expedia, Spotify, Google, eBay, Zillow

🎯 Day 7:


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""

🏆 Solution:
  
 class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(int(len(s) / 2)):
            s = s.replace('()', "").replace("{}", '').replace('[]','')
        return len(s) == 0
            
        
