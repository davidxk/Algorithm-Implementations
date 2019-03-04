#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxSum(vector<int> &A, int size) {
        vector<long long> val(A.size());
        vector<int> len(A.size());
        
        long long maxVal = 0;
        
        val[0] = A[0] > 0 ? A[0] : 0;
        len[0] = A[0] > 0 ? 1 : 0;
        
        maxVal = max(maxVal, val[0]);
        
        for (int i = 1; i < A.size(); i++) {
            long long prevVal = val[i - 1];
            int prevLen = len[i - 1];
            if (prevLen > size - 1) {
                prevVal -= A[i - prevLen];
                prevLen--;
                while (prevLen > 0 && A[i - prevLen] < 0) {
                    prevVal -= A[i - prevLen];
                    prevLen--;
                }
                
            }
            if (prevVal + A[i] > 0) {
                val[i] = prevVal + A[i];
                len[i] = prevLen + 1;
                maxVal = max(val[i], maxVal);
            }
            else {
                val[i] = 0;
                len[i] = 0;
            }
        }
        
        return maxVal;
    }
};

int main()
{
	vector<int> testcase { 999, -1, 1, -100, 10, 1000 };
	Solution sol; 
	cout<<sol.maxSum(testcase, 5)<<endl;
}
