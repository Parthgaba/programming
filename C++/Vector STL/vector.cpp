#include <iostream>
#include <vector>

using namespace std;

void displayVector(vector<int> &v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
}

int main()
{
    int n, element;
    cin >> n;
    vector<int> v;
    vector<char> vChar(6, 'a');
    for (int i = 0; i < n; i++)
    {
        cin >> element;
        v.push_back(element);
    }
    displayVector(v);

    return 0;
}