class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        #split moves -> A moves, B moves
        #only 1 winner so only need to check within A moves or B moves contain valid winning condition
        row_sums = [0] * 3
        col_sums = [0] * 3 
        diag = 0
        anti_d = 0
        for i, [a,b] in enumerate(moves):
            player = 1 if i%2==0 else -1
            row_sums[a] += player
            col_sums[b] += player

            if a == b:
                diag += player
            if a+b == 2:
                anti_d += player
            
            if abs(row_sums[a]) == 3 or abs(col_sums[b]) == 3 or abs(diag) == 3 or abs(anti_d) == 3:
                return "A" if player == 1 else "B"
        print("row: ", row_sums, " col: ", col_sums," diag: ", diag," anti-d: ",anti_d)
        if len(moves) == 9:
            return "Draw"
        
        return "Pending"