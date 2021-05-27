⛓ Link: https://leetcode.com/problems/reverse-integer/
  
 """
💻 List of Companies:Amazon, Facebook, Bloomberg, eBay, American Express
 
🎯 Day 5-
 
 Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
 
 """

🏆 Solution:
  
class Solution:
    def reverse(self, x: int) -> int:
        minus = True if x < 0 else False
        x = x if x >= 0 else -x
        revs=0
        while(x>0):
            rem=x%10
            revs=(revs*10)+rem
            x=x//10
        
        if 2**31-1 >= revs >= -(2**31):
            revs = -revs if minus else revs
            return revs
        else:
            return 0
   
