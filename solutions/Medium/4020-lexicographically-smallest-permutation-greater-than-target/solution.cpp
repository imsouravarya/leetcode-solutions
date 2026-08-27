#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> count(26, 0);
        
        
        for (char c : s) {
            count[c - 'a']++;
        }
        
 
        int matched_len = 0;
        while (matched_len < n && count[target[matched_len] - 'a'] > 0) {
            count[target[matched_len] - 'a']--;
            matched_len++;
        }
        

        int start = min(n - 1, matched_len);
        for (int k = start; k >= 0; k--) {

            if (k < matched_len) {
                count[target[k] - 'a']++;
            }
            

            int next_char = -1;
            for (int c = (target[k] - 'a') + 1; c < 26; c++) {
                if (count[c] > 0) {
                    next_char = c;
                    break; 
                }
            }
    
            if (next_char != -1) {
                string ans = target.substr(0, k); 
                ans += (char)('a' + next_char);  
                count[next_char]--;              
                
   
                for (int c = 0; c < 26; c++) {
                    ans.append(count[c], (char)('a' + c));
                }
                
                return ans;
            }
        }
        

        return "";
    }
};