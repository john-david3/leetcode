class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for l in letters:
            if l > target:
                return l
        return letters[0]