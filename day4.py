⛓ Link:https://leetcode.com/problems/add-strings/

"""

 💻 List of Companies: Facebook, Adobe, Google, Wayfair, Microsoft, Google

 🎯 Day 4-

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

*******************************
 📝 I Didn't understand this question in the first read or the tenth, definetly had to peak into the discussion section to get a few hints.
Also this is a leetcode easy level question apparently.

"""

🏆 Solution:
  
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if n < m:
            num1 = (m-n)*'0' + num1
        if m < n:
            num2 = (n-m)*'0' + num2
        res = 0
        n = len(num1)
        c = 0
        for i,j in zip(num1, num2):
            res += (ord(i)-48 + ord(j)-48)* 10**(n-c-1)
            c += 1
        return str(res) 
