#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int minMoves2(std::vector<int>& nums) {
        // Step 1: Sort the array
        std::sort(nums.begin(), nums.end());
        
        // Step 2: Use two pointers from the ends to the middle
        int left = 0, right = nums.size() - 1;
        int moves = 0;
        
        while (left < right) {
            moves += nums[right] - nums[left];
            left++;
            right--;
        }
        
        return moves;
    }
};