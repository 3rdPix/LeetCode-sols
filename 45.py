class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Starting from the end, search for the greatest jump possible to that point,
        once found, do the same for the found position, continue from there
        """
        jumps: int = 0
        current_position: int = len(nums) - 1
        while current_position != 0:
            greatest_jump: int = current_position
            for distance in range(0, current_position):
                if nums[distance] >= current_position - distance:
                    greatest_jump: int = distance
                    break
            jumps += 1
            current_position = greatest_jump
        return jumps