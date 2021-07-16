#include <iostream>
#include <vector>

using namespace std;

void displayVector(vector<vector<int> > &v)
{
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int size;
    cout << "Enter the size of the vector of vector";
    cin >> size;
    vector<vector<int> > v;
    for (int i = 0; i < size; i++)
    {
        //adding elements to each of the inside vectors
        int inSize;
        cout << "Size of this element vector? ";
        cin >> inSize;
        vector<int> vect;
        for (int j = 0; j < inSize; j++)
        {
            int element;
            cout << "enter the element: ";
            cin >> element;
            vect.push_back(element);
        }
        v.push_back(vect);
    }
    displayVector(v);
    return 0;
}