class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s) -1
        left = 0
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start +=1 
            end -= 1        