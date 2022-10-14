class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for ele in nums2:
            nums1.append(ele)
        nums1.sort()
        x=len(nums1)
        if x%2==0:
            return (nums1[x//2]+nums1[(x//2)-1])/2
        else:
            return nums1[x//2]