class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if max(letters) <= target:

            return letters[0]

        return letters[bisect_right(letters,target)]