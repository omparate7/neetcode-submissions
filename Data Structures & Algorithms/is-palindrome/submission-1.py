class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= 0
        r= len(s)-1

        def alphanumeric(c):
            if (( ord('A') <= ord(c) <= ord('Z') ) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))):
                return True

            return False
        while(r>l):
            while l < r and not alphanumeric(s[l]):
                l+=1
            while l < r and not alphanumeric(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False

            l,r = l+1,r-1
        return True
