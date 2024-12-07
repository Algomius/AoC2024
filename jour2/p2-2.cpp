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
        int n = 0;
        int last = 0;
        string sens = "first";
        int nbErreur = 0;
        s += " ";
        for (char& e : s) {
            if (e == ' ') {
                if (sens == "first") {
                    sens = "None";
                } else if (sens == "None") {
                    if (n > last && abs(n - last) <= 3) {
                        sens = "Croissant";
                    } else if (n < last && abs(n - last) <= 3) {
                        sens = "Decroissant";
                    } else {
                        nbErreur++;
                    }
                } else if (sens == "Croissant") {
                    if (n <= last) {
                        nbErreur++;
                    } else if (abs(n - last) > 3) {
                        nbErreur++;
                    }
                } else if (sens == "Decroissant"){
                    if (n >= last) {
                        nbErreur++;
                    } else if (abs(n- last ) > 3) {
                        nbErreur++;
                    }
                }
                last = n;
                n = 0;
            }
            else 
            {

                n = n * 10 + (e - '0');
            }
        }


        if (nbErreur < 2) {
            somme ++;
        }
    }

    cout << somme << endl;
}