class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lindex: int = 0
        rindex: int = len(nums)
        while lindex < len(nums) and lindex < rindex:
            if nums[lindex] == val:
                rindex = rindex - 1
                while nums[rindex] == val and rindex > -1:
                    rindex = rindex - 1
                if rindex <= lindex: return lindex
                nums[lindex] = nums[rindex]
            lindex = lindex + 1
        return lindex

                
new = Solution()
lista = [0,1,2,2,3,0,4,2]
cantidad = new.removeElement(lista, 2)
print(lista)
print(cantidad)


