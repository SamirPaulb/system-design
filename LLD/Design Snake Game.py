# https://www.lintcode.com/problem/3656/
# https://leetcode.com/problems/design-snake-game/description/
# https://algo.monster/liteproblems/353


from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Initialize the game board with the given width and height
        self.width = width
        self.height = height
      
        # Load the food positions onto the game board
        self.food = deque(food)
      
        # Initialize the score of the game as 0
        self.score = 0
      
        # The snake's body is represented as a queue with initial position at the top-left
        self.snake = deque([(0, 0)])
      
        # A set to keep track of all positions occupied by the snake
        self.snake_positions = set([(0, 0)])

    def move(self, direction: str) -> int:
        # Get the snake's current head position
        head_row, head_col = self.snake[0]
      
        # Move based on the provided direction
        if direction == 'U':
            head_row -= 1
        elif direction == 'D':
            head_row += 1
        elif direction == 'L':
            head_col -= 1
        elif direction == 'R':
            head_col += 1
      
        # Check if the new position is out of bounds
        if head_row < 0 or head_row >= self.height or head_col < 0 or head_col >= self.width:
            return -1
      
        # Check if the snake has moved to a cell containing food
        if self.food and [head_row, head_col] == self.food[0]:
            self.food.popleft()  # Eat the food
            self.score += 1      # Increase the score
        else:
            # Remove the tail if no food is eaten
            tail = self.snake.pop()
            self.snake_positions.remove(tail)
      
        # Check if the snake crashes into itself
        if (head_row, head_col) in self.snake_positions:
            return -1
      
        # Add the new head position of the snake
        self.snake.appendleft((head_row, head_col))
        self.snake_positions.add((head_row, head_col))
      
        # Return the current score of the game
        return self.score


# Example of how to instantiate and use the class
# game = SnakeGame(width, height, food)
# score = game.move(direction)
