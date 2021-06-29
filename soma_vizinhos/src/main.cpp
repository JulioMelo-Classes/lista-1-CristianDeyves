#include <iostream>
using std::cout;
using std::cin;
using std::endl;

/*
não entendi bem qual sua ideia aqui, mas o resultado é bem diferente do esperado por isso vou considerar 10%
*/
int main( void )
{
    int num[2] = {0}, temp = 0;


    
    while (cin >> std::ws >> num[0] >> num[1])
    {
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
    }
    

    return 0;
}