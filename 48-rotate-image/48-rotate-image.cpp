#include<iostream>
using namespace std;
class Solution {
public:
	void transpose(vector<vector<int>>& matrix)
	{
		for(int i=0;i<matrix.size();i++)
		{
			for(int j=i+1;j<matrix[0].size();j++)
			{
				swap(matrix[i][j],matrix[j][i]);
			}
		}
	}

	void reverseRows(vector<vector<int>>& matrix)
	{
		for(int i=0;i<matrix.size();i++)
		{
			reverse(matrix[i].begin(),matrix[i].end());
		}
	}
	void rotate(vector<vector<int>>& matrix) {
		//rotate 90 clockwise=transpose+reverse
		transpose(matrix),reverseRows(matrix);
	}
};