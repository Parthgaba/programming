#include <iostream>
#include <vector>

using namespace std;

bool validMountainArray(vector<int> &arr)
{
    int mx = INT_MIN;
    int mxi = -1;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] > mx)
        {
            mx = arr[i];
            mxi = i;
        }
    }
    if (mxi == arr.size() - 1 || mxi == 0)
    {
        return false;
    }
    int i = 1;
    int j = arr.size() - 1;
    while (1)
    {

        if (!(arr[i - 1] < arr[i]))
        {
            return false;
        }
        if (!(arr[j - 1] > arr[j]))
        {
            return false;
        }
        if (j - 1 > mxi)
        {
            j--;
        }
        if (i < mxi)
        {
            i++;
        }
        if ((!(i < mxi)) && (!(j - 1 > mxi)))
        {
            break;
        }
    }
    /*
    for (int i = 1; i < mxi; i++)
    {
        if (!(arr[i - 1] < arr[i]))
        {
            return false;
        }
    }

    for (int i = mxi; i < arr.size() - 1; i++)
    {
        if (!(arr[i] > arr[i + 1]))
        {
            return false;
        }
    }*/
    return true;
}

int main()
{
    int arr[] = {3, 5, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> v(arr, arr + n);
    cout << validMountainArray(v) << endl;
    return 0;
}