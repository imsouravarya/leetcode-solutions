class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[pixel ^ 1 for pixel in row[::-1]] for row in image]