#include <iostream>

using namespace std;

int main()
{
    int n = 0, sum = 0;
    while (true)
    {
        cin >> n;
        if (n == 0)
        {
            break;
        }
        else
        {
            for (int i = 1; i < n + 1; i++)
            {
                sum += i * i;
            }
        }
        cout << sum << endl;
        sum = 0;
    }
    return 0;
}