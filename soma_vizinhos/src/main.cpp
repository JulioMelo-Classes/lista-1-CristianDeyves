#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main( void )
{
    int num[2] = {0}, temp = 0;

    cout << "Digite um numero inteiro de para referencia: " << endl;
    cin >> num[1];

    cout << "Digite um numero inteiro, para somar os anterios ou posteriores do numero de referencaia: " << endl;
    cin >> num[2];

    if (num[2] > 0)
    {
        while (temp != num[2])
        {
            num[1]++, temp++;
        }
        cout << "A soma dos antecedente/posteriores e: " << num[1] << endl;
    }

    else if (num[2] = 0)
    {
        cout << "A soma dos antecedente/posteriores e: " << num[1] << endl;
    }

    else
    {
        while (temp != num[2])
        {
            num[1] = num[1] + (num[1] -1);
            temp++;
        }
        cout << "A soma dos antecedente/posteriores e: " << num[1] << endl;
    }

    return 0;
}