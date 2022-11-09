class Solution:
    def rob(self, nums: List[int]) -> int:
	# we have 0 dollars after robbing no houses and nums[0] dollars after robbing the first house
	    last_two = (0, nums[0])
	# go through the rest of the houses
	    for i in range(1, len(nums)):
		# if we rob this house
		    rob_this_house = nums[i] + last_two[0]
		# if we dont
		    dont_rob_this_house = last_two[1]
		# update the amt of money we could have gotten from the last two houses
		    last_two = (last_two[1], max(rob_this_house, dont_rob_this_house))
	# return money after robbing all the houses
	    return last_two[1]