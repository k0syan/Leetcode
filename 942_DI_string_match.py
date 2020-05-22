class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        first = 0
        last = len(S)
        ans = []
        for c in S:
            if c == 'I':
                ans.append(first)
                first += 1
            else:
                ans.append(last)
                last -= 1

        return ans + [first]
