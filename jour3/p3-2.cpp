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
    bool enable = true;

    while (getline(monFichier, s)) {
        for (int indice = 0;indice<s.size()-4;indice++){
            if (s.substr(indice,4) == "mul(") {
                int n1 = 0;
                int i= 4;

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

                    if (s[indice + i] == ')' && n2 < 1000 && enable) {
                        somme += n1 * n2;
                    }

                }
            } else if (s.substr(indice,4) == "do()") {
                enable = true;
            } else if (s.substr(indice,7) == "don't()") {
                enable = false;
            }
        }
    }

    cout << somme << endl;
}