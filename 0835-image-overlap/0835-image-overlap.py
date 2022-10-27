class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """

        # return 0 if img1 is empty
        if len(img1) == 0:
            return 0

        # create sets of indices that are one 
        idx1 = set()
        for i,_ in enumerate(img1):
            for j,_ in enumerate(img1[i]):
                if img1[i][j] == 1:
                    idx1.add((i,j))
                
        idx2 = set()
        for i, _ in enumerate(img2):
            for j, _ in enumerate(img2[i]):
                if img2[i][j] == 1:
                    idx2.add((i,j))


        # add the shift to the indices
        def shift_and_count(shift_hor, shift_ver):
            shifted_idx1 = set()
            for (h,v) in idx1:
                shifted_idx1.add((h+shift_hor,v+shift_ver))
        
            # compute the intersection of the shifted set and img2 as this is the number of overlapping ones
            return len(shifted_idx1.intersection(idx2))


        max_value = 0

        for shift_hor in range(-len(img1), len(img1)):
            for shift_ver in range(-len(img1), len(img1)):
                max_value = max(max_value, shift_and_count(shift_hor, shift_ver))

        return max_value