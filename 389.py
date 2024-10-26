class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter, appearances in collections.Counter(t).items():
            if appearances > s.count(letter): return letter