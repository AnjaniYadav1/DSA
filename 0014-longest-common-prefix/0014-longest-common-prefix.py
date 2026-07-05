class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        ans = ""
        a=sorted(a)
        first=a[0]
        last=a[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans

