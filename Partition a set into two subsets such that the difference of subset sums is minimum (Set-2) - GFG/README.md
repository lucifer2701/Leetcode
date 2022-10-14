# Partition a set into two subsets such that the difference of subset sums is minimum (Set-2)
## Hard
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a set of n integers, divide the set in two subsets, S1 and S2, of n/2 sizes each such that the difference of the sum of two subsets is as minimum as possible. The task is to print that two subset S1 and S2. Elements in S1 and S2 should be present in same format as given in input.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;</span></p>

<ol>
	<li><span style="font-size:18px">If n is even, then sizes of two subsets must be strictly n/2 </span></li>
	<li><span style="font-size:18px">if n is odd, then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.</span></li>
</ol>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> arr[] = {3, 4, 5, -3, 100, 
1, 89, 54, 23, 20}
<strong>Output: </strong>S1 = {4, 100, 1, 23, 20} 
S2 = {3, 5, -3, 89, 54}
<strong>Explanation:</strong>  Both output subsets 
are of size 5 and sum of elements in 
both subsets is same (148 and 148).
So the minimum difference will be 0.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> arr[] = {23, 45, -34, 12, 0, 
98, -99, 4, 189, -1, 4}
<strong>Output:</strong> S1 = {45, -34, 12, 98, -1} 
 S2 = {23, 0, -99, 4, 189, 4}
<strong>Explanation:</strong> The sums of elements in 
two subsets are 120 and 121 respectively.
So the minimum difference will be 1.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Complete the function&nbsp;<strong><code>minDifference</code>()&nbsp;</strong>which takes&nbsp;<strong>N</strong>&nbsp;and array&nbsp;<strong>arr&nbsp;</strong>as input parameters and returns the arrays.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(2^N)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(2*N)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 30<br>
-10000 &lt;= arr[i] &lt;= 10000</span></p>
</div>