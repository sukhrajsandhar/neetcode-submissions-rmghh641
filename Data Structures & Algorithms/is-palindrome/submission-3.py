class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        reverse += s
        reverse = reverse[::-1]
        reverse = reverse.lower()
        reverse = re.sub(r'[^A-Za-z0-9]', '', reverse)
        
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]', '', s)

        return reverse == s