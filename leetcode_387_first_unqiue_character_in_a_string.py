class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = Counter(s)
        for i in range(len(s)):
            if count_map[s[i]] == 1:
                return i
        return -1
