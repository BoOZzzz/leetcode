class Solution:
    def checkRecord(self, s: str) -> bool:
        # most intuitive way, counter check for both absent and late. check condition after 1 iteration
        absent = 0
        late = 0
        for c in s:
            if c == 'A':
                absent += 1
            if c == 'L':
                late += 1
            else:
                late = 0
            if late == 3:
                return False
        return absent < 2