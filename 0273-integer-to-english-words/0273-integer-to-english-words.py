class Solution:
	def numberToWords(self, num: int) -> str:
		if num == 0:
			return 'Zero'
    
		rec = {
			10**9: "Billion",
			10**6: "Million",
			10**3: "Thousand",
			10**2: "Hundred",
			1: "One",
			2: "Two",
			3: "Three",
			4: "Four",
			5: "Five",
			6: "Six",
			7: "Seven",
			8: "Eight",
			9: "Nine",
			10: "Ten",
			11: "Eleven",
			12: "Twelve",
			13: "Thirteen",
			14: "Fourteen",
			15: "Fifteen",
			16: "Sixteen",
			17: "Seventeen",
			18: "Eighteen",
			19: "Nineteen",
			20: "Twenty",
			30: "Thirty",
			40: "Forty",
			50: "Fifty",
			60: "Sixty",
			70: "Seventy",
			80: "Eighty",
			90: "Ninety"}
		keys = sorted(rec.keys(), reverse = True)

		def recursion(n):
			ans = ""
			while n > 0:
				for k in keys:
					if n >= k:
						t = n//k
						n -= k*t
						if t > 1:
							ans += recursion(t) 
						else:
							if k in (10**9, 10**6, 10**3, 10**2):
								ans += "One "
						ans += rec[k] + " "

			return ans

		return recursion(num).strip()