#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main( void )
{
    int num[2] = {0}, temp = 0;

    cin >> num[0];

    cin >> num[1];

    if (num[1] > 0)
    {
        while (temp != num[1])
        {
            num[0]++;
            temp++;
        }
        cout << num[0] << endl;
    }

    else if (num[1] = 0)
    {
        cout << num[0] << endl;
    }

    else
    {
        while (temp != num[1])
        {
            num[0] = num[0] + (num[0] - 1);
            temp++;
        }
        cout << num[0] << endl;
    }

    return 0;
}