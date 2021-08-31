#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int n = nums.size();
        int res = 0;
        vector<int> v;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] == val)
                res++;
            else
                v.push_back(nums[i]);
        }
        for (int j = 0; j < n; j++)
        {
            if (j < (n - res))
            {
                nums[j] = v[j];
            }
            else
                nums[j] = -1;
        }
        return n - res;
    }
};