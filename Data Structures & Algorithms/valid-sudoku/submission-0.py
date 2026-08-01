class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for arr in board:
            if self.containDubs(arr):
                return False

        # Check columns
        for col in range(9):
            arrCol = [board[row][col] for row in range(9)]
            if self.containDubs(arrCol):
                return False

        # Check 3x3 boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[boxRow + i][boxCol + j])
                if self.containDubs(box):
                    return False

        return True

    def containDubs(self, arr):
        seenSet = set()
        for item in arr:
            if item == ".":
                continue
            if item in seenSet:
                return True
            seenSet.add(item)
        return False