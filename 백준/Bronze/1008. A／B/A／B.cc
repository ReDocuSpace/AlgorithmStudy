#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(NULL);
	cin.tie(NULL);

	double num1;
	double num2;

	cin >> num1 >> num2;
	cout << fixed;
	cout.precision(15);
	cout << (num1 / num2);

}