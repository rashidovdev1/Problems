#include <iostream>
using namespace std;

int main(){
	float r,L,S, pi=3.14;
    cout << "R ni kiriting: "; cin >> r;
    
    L = 2 * pi * r;
    S = pi * r * r;
    
    cout << "Uzunligi: " << L << endl;
 	cout << "Yuzasi: " << S << endl;
	return 0;
}
