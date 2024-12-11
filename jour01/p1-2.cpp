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
    vector<int> first;
    vector<int> last;

    string s;
    while (getline(monFichier, s)) {
        stringstream ligne(s);
        
        string firstValue;
        string lastValue;
        getline(ligne, firstValue, ' ');
        getline(ligne, lastValue);
        first.push_back(stoi(firstValue));
        last.push_back(stoi(lastValue));

    }
    std::sort(first.begin(), first.end());
    std::sort(last.begin(), last.end());

    int somme = 0;

    for(int i = 0;i< first.size();i++) {
        somme += first[i]*count (last.begin(), last.end(), first[i]);
    }

    cout << somme << endl;
}