class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        writePointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writePointer] = nums[i]
                if writePointer != i:
                    nums[i] = 0
                writePointer += 1
