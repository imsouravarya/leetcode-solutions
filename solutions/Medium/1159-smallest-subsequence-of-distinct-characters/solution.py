class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last_index = {char: i for i, char in enumerate(s)}
        
        result = []
        
        for i, char in enumerate(s):

            if char in result:
                continue
                

            while result and char < result[-1] and last_index[result[-1]] > i:
                result.pop()
                

            result.append(char)
            
        return "".join(result)