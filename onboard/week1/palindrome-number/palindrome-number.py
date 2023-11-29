class Solution:
    def isPalindrome(self, x: int) -> bool:

        update_string = str(x)

        return True if update_string[::-1] == update_string else False
        