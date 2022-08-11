def merge_arrays(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    [2,0], [1]
    """
    # nums1[:] = sorted(nums1[:m] + nums2)
    for i in range (m,m+n):
        nums1[i] = nums2[i-m]
    nums1.sort()
    return nums1

print(merge_arrays([1,2,3,0,0,0], 3, [2,5,6], 3))
