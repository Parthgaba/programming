#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        if (n == 0)
        {
            return 0;
        }
        vector<int> v;
        v.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i - 1] == nums[i])
            {
                continue;
            }
            v.push_back(nums[i]);
        }
        int res_size = v.size();
        for (int j = 0; j < nums.size(); j++)
        {
            if (j < res_size)
            {
                nums[j] = v[j];
            }
            else
            {
                nums[j] = -101;
            }
        }
        return res_size;
    }
};
