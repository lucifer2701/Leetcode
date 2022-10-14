class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        sum = len(nums1) + len(nums2)
        if sum % 2 != 0:
            sum2 = int(sum / 2)
            return nums[sum2]
        else:
            sum3 = int(sum / 2)
            sum4 = (nums[sum3] + nums[sum3-1]) / 2 
            return sum4