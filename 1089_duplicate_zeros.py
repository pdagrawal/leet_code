class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        Input: arr = [1,0,2,3,0,4,5,0]
        Output: [1,0,0,2,3,0,0,4]
        """
        i = 0
        while i <= len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i+1, 0)
                i += 1
            i += 1
            if i >= len(arr):
                break
