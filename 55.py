class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # conjunto conexo o unicidad
        if (0 not in nums) or (len(nums) == 1): return True

        # la única forma de no poder llegar es que exista una "pared" 0 en algún sitio
        # esta pared debe no ser saltable

        zero_indexes: list = [index for index, number in enumerate(nums) if number == 0]
        for zero in zero_indexes:
            jumpable: bool = False
            for distance in range(1, zero + 1):
                if nums[zero - distance] > distance:
                    jumpable: bool = True
                    break
                elif nums[zero - distance] == distance and zero == len(nums) - 1:
                    jumpable: bool = True
                    break
            if not jumpable: return False
        return True