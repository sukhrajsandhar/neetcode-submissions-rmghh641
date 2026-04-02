class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        reverse += s
        reverse = reverse.lower()
        reverse = re.sub(r'[^A-Za-z0-9]', '', reverse)
        
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]', '', s)

        print(s)
        print(reverse)

        return reverse == s