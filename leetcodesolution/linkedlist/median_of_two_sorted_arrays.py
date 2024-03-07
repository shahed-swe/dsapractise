def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to minimize the binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2
    l, r = 0, m

    while l <= r:
        i = (l + r) // 2
        j = half - i

        maxLeftA = float("-inf") if i == 0 else nums1[i - 1]
        minRightA = float("inf") if i == m else nums1[i]

        maxLeftB = float("-inf") if j == 0 else nums2[j - 1]
        minRightB = float("inf") if j == n else nums2[j]

        # Correct partition
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if total % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
        # Adjust search range
        elif maxLeftA > minRightB:
            r = i - 1
        else:
            l = i + 1


# Test cases
# print(findMedianSortedArrays([1, 3], [2]))  # Example 1
print(findMedianSortedArrays([1, 2], [3, 4]))  # Example 2
