class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #easiest way double for loops
        count = 0
        for w in words:
            same = True
            if len(w) < len(pref):
                continue
            for i in range(len(pref)):
                if w[i] != pref[i]:
                    same = False
                    break
            if same:
                count += 1

        return count