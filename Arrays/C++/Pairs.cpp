#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
//Time Complexity = O(n)
//Space Complexity = O(n)
int countPairs(vector<int> &v, int k)
{
    unordered_map<int, int> map;
    int count = 0;
    for (int i = 0; i < v.size(); i++)
    {
        map[v[i]]++;
    }
    for (int i = 0; i < v.size(); i++)
    {
        count += map[k - v[i]];
        if (map[k - v[i]] != 0)
        {
            cout << k - v[i] << " " << v[i] << endl;
        }
        if (k - v[i] == v[i])
        {
            count--;
        }
    }
    return count / 2;
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
         << countPairs(v, 7) << endl;
    return 0;
}