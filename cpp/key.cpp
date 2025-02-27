#include <bits/stdc++.h>
using namespace std;

int main()
{
    string input = "578378923";
    unordered_set<char> seen;  // To store unique characters
    unordered_set<char> duplicates;  // To store duplicate characters

    for (char c : input)
    {
        if (seen.find(c) != seen.end())  // If already in seen, it's a duplicate
        {
            duplicates.insert(c);
        }
        else
        {
            seen.insert(c);  // Add to seen for the first time
        }
    }


    cout << "Number of duplicate characters: " << duplicates.size() << endl;

    return 0;
}
