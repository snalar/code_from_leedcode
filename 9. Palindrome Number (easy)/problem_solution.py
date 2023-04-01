class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x)[:((len(str(x))) // 2)] == (str(x)[(((len(str(x)) - 1) // 2) + 1):])[::-1])
