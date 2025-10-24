// V=a*b*c & S=2*(a*b+b*c+a*c)
#include<iostream>
using namespace std;

int main() {
 int a, b, c, S, V;
 cout << "A ni kiriting: "; cin >> a;
 cout << "B ni kiriting: "; cin >> b;
 cout << "C ni kiriting: "; cin >> c;

 S = 2 * (a * b + b * c + a * c);
 V = a * b * c;

 cout << "To'la sirti: " << S << endl;

 cout << "Hajmi: " << V << endl;

 return 0;
}
