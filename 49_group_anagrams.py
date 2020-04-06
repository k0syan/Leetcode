class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            so = "".join(sorted(s))
            print(so)
            if so in d:
                d[so].append(s)
            else:
                d[so] = [s]
        return d.values()
