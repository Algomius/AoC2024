#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;

int main() {
    fstream monFichier("input.txt", ios::in);

    string s;
    int somme = 0;

    while (getline(monFichier, s)) {
        size_t indice = s.find("mul(");
        while (indice !=std::string::npos) {
            indice += 4;
            int n1 = 0;
            int i= 0;

            while (s[indice + i] >= '0' && s[indice + i] <= '9') {
                n1 = n1 * 10 + (s[indice + i] - '0');
                i++;
            }
            
            if (s[indice + i] == ',' && n1 < 1000) {
                i += 1;
                int n2 = 0;
                while (s[indice + i] >= '0' && s[indice + i] <= '9') {
                    n2 = n2 * 10 + (s[indice + i] - '0');
                    i += 1;
                }

                if (s[indice + i] == ')' && n2 < 1000) {
                    somme += n1 * n2;
                }

            }

            s = s.substr(indice);
            indice = s.find("mul(");
        }
    }

    cout << somme << endl;
}