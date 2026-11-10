class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# s = "racecar"
# t = "carrace"
        if len(s) == len(t):
            s_chars = list(s)
            counts = {}
            for char in s_chars:
                counts[char] = counts.get(char, 0) + 1
            
            t_counts = {}
            for char in t:
                t_counts[char] = t_counts.get(char, 0) + 1
            return counts == t_counts
        else:
            return False
