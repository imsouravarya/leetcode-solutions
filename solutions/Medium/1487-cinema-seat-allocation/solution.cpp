#include <vector>
#include <unordered_map>

class Solution {
public:
    int maxNumberOfFamilies(int n, std::vector<std::vector<int>>& reservedSeats) {
        std::unordered_map<int, int> rowMasks;

        // Step 1: Record reservations for seats 2 to 9
        for (const auto& seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            if (col >= 2 && col <= 9) {
                rowMasks[row] |= (1 << col);
            }
        }

        // Bitmasks for seating options
        int leftMask   = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5); // Seats 2, 3, 4, 5
        int rightMask  = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9); // Seats 6, 7, 8, 9
        int middleMask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7); // Seats 4, 5, 6, 7

        // Step 2: Unreserved rows (or rows only reserved at seats 1/10) hold 2 families each
        int totalFamilies = (n - rowMasks.size()) * 2;

        // Step 3: Process rows with reservations
        for (const auto& [row, mask] : rowMasks) {
            bool leftFree   = !(mask & leftMask);
            bool rightFree  = !(mask & rightMask);
            bool middleFree = !(mask & middleMask);

            if (leftFree && rightFree) {
                totalFamilies += 2;
            } else if (leftFree || rightFree || middleFree) {
                totalFamilies += 1;
            }
        }

        return totalFamilies;
    }
};