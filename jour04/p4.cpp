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

    int cpt = 0;
    for (int i = 0; i < v.size();i++) {
        for (int j = 0; j < v[0].size();j++) {
            if (v[i][j] == 'X') {
                for (int decH = -1; decH <= 1; decH++) {
                    for (int decV = -1; decV <= 1; decV++) {
                        if (i+(3*decH) >= 0 && i+(3*decH) < v[0].size() && j+(3*decV) >= 0 && j+(3*decV) < v.size()) {
                            if (v[i+(1*decH)][j+(1*decV)] == 'M' && 
                                v[i+(2*decH)][j+(2*decV)] == 'A' && 
                                v[i+(3*decH)][j+(3*decV)] == 'S') {
                                    cpt++;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << cpt << endl;
}