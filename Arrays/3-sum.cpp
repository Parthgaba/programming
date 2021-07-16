#include <iostream>
#include <vector>

using namespace std;
//Time Complexity = O(n^2)
//Space Complexity = O(1)
int count3Sum(vector<int> &v, int k)
{
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size() - 1; i++)
    {
        int start = i + 1;
        int end = v.size() - 1;
        int low = v[start];
        int high = v[end];
        while (start < end)
        {
            int res = low + high;
            if (res + v[i] == k)
            {
                return 1;
            }
            if ((res + v[i]) < k)
            {
                start++;
            }
            else
            {
                end--;
            }
            low = v[start];
            high = v[end];
        }
    }
    return 0;
}

int main()
{
    vector<int> v;
    for (int i = 0; i < 12; i++)
    {
        v.push_back(i + 1);
        cout << i + 1 << " ";
    }
    cout << endl
         << count3Sum(v, 7) << endl;
    return 0;
}