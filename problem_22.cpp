//Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

//For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

//What is the total of all the name scores in the file?

#include <fstream>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

bool compare(string a, string b)
{
    return strcmp(a.c_str(), b.c_str()) < 0;
}

using namespace std;

vector<string> names;

unsigned long long name_score(unsigned long long index, string name)
{
    unsigned long long sum = 0;
    for (size_t i = 0; i < name.size(); ++i) {
        sum += (name[i] - 'A') + 1;
    }
    return index * sum;
}

int main()
{
    unsigned long long total = 0;

    ifstream file("names.txt");
    while (!file.eof()) {
        string input;
        file >> input;
        if (input.size() != 0) {
            names.push_back(input);
        }
    }

    sort(names.begin(), names.end(), compare);
    for (size_t i = 0; i < names.size(); ++i) {
        unsigned long long score = name_score(i + 1, names[i]);
        cout << names[i] << ": " << score << endl;
        total += score;
    }

    cout << "The total score is " << total << endl;
}
