class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s = s.lower()
        # if len(s)==2:
        #     return false
        print(i,j)
        while i<j:
            # print(s[i].isalpha(),s[j].isalpha())
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            # print(s[i],s[j])
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        