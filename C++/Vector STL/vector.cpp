#include <iostream>
#include <vector>

void display(vector<int> &v)
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
    for (int i = 0; i < n; i++)
    {
        cin >> element;
        vector.push_back(element);
    }
    diplay(v);

    return 0;
}