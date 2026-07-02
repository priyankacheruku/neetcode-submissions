class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            current_s = str(len(s))+"#"+s
            res.append(current_s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i= 0
        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            l = int(s[i:j])
            j+=1 #for #
            res.append(s[j:j+l])
            i = j+l
        return res
