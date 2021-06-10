#include <iostream>
using namespace std;

const int SIZE = 5; // input size.

int main(void)
{
    int cont[2] = {0}, vector[SIZE];

    while (cont[1] < SIZE)
    {
        cout << "Digite um numero inteiro:" << endl;

        cin >> vector[cont[1]];

        if (vector[cont[1]] < 0)
        {
            cont[0]++;
        }

        cont[1]++;
        
    }

    if (cont[0] > 1)
    {
        cout << "Dentre os numeros digitados, sao negativos: " << cont[0] << endl;
    }
    else
    {
        cout << "Dentre os numeros digitados, e negativo: " << cont[0] << endl;
    }

    return 0;
}