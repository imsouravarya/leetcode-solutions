class Solution {
public:
    int missingInteger(vector<int>& nums) {
        // Step 1: Calculate the sum of the longest sequential prefix
        int currentSum = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1] + 1) {
                currentSum += nums[i];
            } else {
                break; // Sequential chain stopped
            }
        }

        // Step 2: Store nums in a set for O(1) lookup
        unordered_set<int> st(nums.begin(), nums.end());

        // Step 3: Find the smallest integer >= currentSum NOT in nums
        while (st.count(currentSum)) {
            currentSum++;
        }

        return currentSum;
    }
};