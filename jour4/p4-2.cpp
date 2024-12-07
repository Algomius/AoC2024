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
    vector<string> v;

    while (getline(monFichier, s)) {
        v.push_back(s);
    }

    for (int i = 1; i < v.size()-1;i++) {
        for (int j = 1; j < v[0].size()-1;j++) {
            if (v[i][j] == 'A') {
                int cpt = 0;
                for (int decH : {-1, 1}) {
                    for (int decV : {-1, 1}) {
                        if (v[i+decH][j+decV] == 'M' && v[i+(-1*decH)][j+(-1*decV)] == 'S') {
                            cpt++;
                        }
                    }
                }
                if (cpt == 2) {
                    somme++;
                }
            }
        }
    }
    cout << somme << endl;
}