class Solution:
    def isValid(self, s: str) -> bool:
        # Keep replacing valid matching pairs as long as they exist
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        
        # If all valid pairs were matched and stripped, s will be empty
        return s == ""