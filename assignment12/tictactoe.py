# Task 6: More on Classes

class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Board:
    valid_moves = ["upper left", "upper center", "upper right",
                   "middle left", "center", "middle right",
                   "lower left", "lower center", "lower right"]
    
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = [
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} ",
            "-----------",
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} ",
            "-----------",
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} "
        ]
        return "\n".join(lines)
    
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        idx = Board.valid_moves.index(move_string)
        row, col = divmod(idx, 3)
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][col] = self.turn
        self.last_move = move_string
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check rows, columns, diagonals
        for i in range(3):
            if self.board_array[i][0] != " " and len(set(self.board_array[i])) == 1:
                return (True, f"{self.board_array[i][0]} wins!")
            col = [self.board_array[j][i] for j in range(3)]
            if col[0] != " " and len(set(col)) == 1:
                return (True, f"{col[0]} wins!")
        if self.board_array[0][0] != " " and self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
            return (True, f"{self.board_array[0][0]} wins!")
        if self.board_array[0][2] != " " and self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
            return (True, f"{self.board_array[0][2]} wins!")
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game.")
        return (False, f"{self.turn}'s turn.")

if __name__ == "__main__":
    board = Board()
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print(board)
        move = input(f"{board.turn}'s move: ").lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(e.message)
            continue
        over, message = board.whats_next()
        if over:
            print(board)
            print(message)
            break
