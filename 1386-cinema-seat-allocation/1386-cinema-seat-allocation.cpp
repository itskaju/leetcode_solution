#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {

        unordered_map<int, int> mp;

        // store seats as bitmask
        for (auto &seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];

            // only care seats 2 to 9
            if (col >= 2 && col <= 9) {
                mp[row] |= (1 << col);
            }
        }

        int total = 0;

        // rows WITHOUT reservations
        total += (n - mp.size()) * 2;

        for (auto &it : mp) {
            int mask = it.second;

            bool left  = (mask & ((1<<2)|(1<<3)|(1<<4)|(1<<5))) == 0;
            bool right = (mask & ((1<<6)|(1<<7)|(1<<8)|(1<<9))) == 0;
            bool mid   = (mask & ((1<<4)|(1<<5)|(1<<6)|(1<<7))) == 0;

            if (left) total++;
            if (right) total++;
            else if (!left && mid) total++;
        }

        return total;
    }
};