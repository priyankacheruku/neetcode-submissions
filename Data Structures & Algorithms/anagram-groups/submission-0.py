class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # def check_anagram(w1,w1):
        #     if w1.sort()==w2.sort():
        #         return True
        data = {}
        for each_word in strs:
            curr = ''.join(sorted(each_word))
            # print(curr)
            if data.get(curr):
                data[curr].append(each_word)
            else:
                data[curr] = [each_word]
        res = []
        for key,value in data.items():
            res.append(value)
        return res
        


            
        