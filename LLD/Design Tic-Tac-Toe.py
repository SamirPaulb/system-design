# https://www.geeksforgeeks.org/low-level-design-of-tic-tac-toe-system-design/

class TicTacToe:
	def __init__(self):
		self.board = [[' ' for _ in range(3)] for _ in range(3)]
		self.current_player = 1

	def print_board(self):
		for row in self.board:
			print('|'.join(row))
			print('-' * 5)

	def is_board_full(self):
		return all(cell != ' ' for row in self.board for cell in row)

	def make_move(self, row, column):
		if 0 <= row < 3 and 0 <= column < 3 and self.board[row][column] == ' ':
			self.board[row][column] = 'X' if self.current_player == 1 else 'O'
			# Switch player (1 to 2 or 2 to 1)
			self.current_player = 3 - self.current_player
			return True
		return False

	def check_winner(self):
		for i in range(3):
			if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
				return True # Row win
			if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
				return True # Column win
		if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
			return True # Diagonal win
		if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
			return True # Diagonal win
		return False


# Main game loop
if __name__ == "__main__":
	game = TicTacToe()

	while not game.is_board_full() and not game.check_winner():
		game.print_board()

		row, column = map(int, input(
			f"Player {game.current_player}, enter your move (row and column): ").split())

		if game.make_move(row, column):
			print("Move successful!")
		else:
			print("Invalid move. Try again.")

	game.print_board()

	if game.check_winner():
		print(f"Player {3 - game.current_player} wins!")
	else:
		print("It's a draw!")
