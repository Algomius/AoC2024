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
        bool test = true;
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
                        test = false;
                    }
                } else if (sens == "Croissant") {
                    if (n <= last) {
                        test = false;
                    } else if (abs(n - last) > 3) {
                        test = false;
                    }
                } else if (sens == "Decroissant"){
                    if (n >= last) {
                        test = false;
                    } else if (abs(n- last ) > 3) {
                        test = false;
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


        if (test) {
            somme ++;
        }
    }

    cout << somme << endl;
}