
#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size() - 1; i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums.at(i) + nums.at(j) == target) return { i,j };
        }
    }
    return { -1,-1 };
}

int main() {
  
    vector<int> arr = { 1, 3, 5, 12, 2, 9, 4, 7, 11 };
    int target = 12;

    vector<int> sol = twoSum(arr, target);

    cout << "solution: ";
    for (int i : sol) {
        cout << i << " ";
    }

    return 0;
}