class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for dom in cpdomains:
            cnt, tmp = dom.split()[0], dom.split()[1].split(".")
            t = tmp[len(tmp) - 1]
            for i in range(len(tmp)-1, -1, -1):
                if i != len(tmp) - 1:
                    t = tmp[i] + "." + t
                if t in d:
                    d[t] += int(cnt)
                else:
                    d[t] = int(cnt)
        ans = []
        for t in d:
            ans.append(str(d[t]) + " " + t)
        return ans
