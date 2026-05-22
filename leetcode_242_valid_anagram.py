class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1 = Counter(s)
        map_2 = Counter(t)
        if len(s) != len(t):
            return False
        return map_1 == map_2