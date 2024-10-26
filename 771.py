class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count: int = 0
        for stone in stones:
            count += 1 if stone in jewels else 0
        return count
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        amount: int = 0
        for each in jewels:
            amount += stones.count(each)
        return amount
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        amount: int = 0
        index: int = 0
        while index < len(jewels):
            amount += stones.count(jewels[index])
            index += 1
        return amount