import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[\W+_]', '', s).lower()

        l, r = 0, len(s) - 1 
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
    print(Solution().isPalindrome('race'))
    print(Solution().isPalindrome('racecar'))