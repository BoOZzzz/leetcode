class Solution:
    def reorderSpaces(self, text: str) -> str:
        #count the number of spaces
        words = text.split()
        count = 0 #count the length of the words, subtract away from total len to get #spaces
        for w in words:
            count += len(w)
        num_spaces = len(text) - count
        if count == len(text):
            return text
        modified = words[0]
        if len(words) != 1:
            gap_len = num_spaces // (len(words)-1)
            for i in range(1, len(words)):
                modified += " " * gap_len
                modified += words[i]
                num_spaces -= gap_len
        modified += " " * num_spaces
        return modified
        