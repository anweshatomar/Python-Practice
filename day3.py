Link:

"""
Day 3-

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

Failed Solution:
 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        init=[]
        in_num=[]
        for i in words:
            init.append(i[0])
        for j in range(0,len(order)):
            for k in range(0,len(init)):
                if init[k]==order[j]:
                    in_num.append(j)
        for l in range(0,len(in_num)):
            for m in range(0,l):
                if in_num[m]<=in_num[l]:
                    return True 
                else:
                    return False
                  
Working Solution:
  
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        l1 = {c:i for i,c in enumerate(order)}
        l2 = [[l1[i] for i in word] for word in words]
        return l2 == sorted(l2)
  
