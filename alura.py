import tkinter as tk
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CANVAS_RES = 25  # Resolution of one tile

class Snake:
    def __init__(self):
        self.position = [(0, 0), (CANVAS_RES, 0), (CANVAS_RES * 2, 0)]  # list of segment positions
        self.direction = (1, 0)  # cosine and sine of current direction
        self.direction_buffer = None
        self.direction_received = True
        self.fill_body = "#FF0000"
        self.fill_head = "#993333"
        self.outline = "#000000"

    def move(self, food):
        """"
        Updates position vector of snake in moving direction.
            - If new head position is outside canvas, wrap around.
            - If new head position equals position of current food, grow by one segment
            - If new head position is in existing position, the game is over
        Returns:
            bool: Indicater whether self-collision has occurred
        """
        x_head, y_head = self.position[-1]
        x_new = (x_head + self.direction[0] * CANVAS_RES) % CANVAS_WIDTH
        y_new = (y_head + self.direction[1] * CANVAS_RES) % CANVAS_HEIGHT
        position_new = (x_new, y_new)
        if position_new in self.position:
            return (True)  # Self collision

        self.position.append(position_new)
        if not position_new == food.position:
            self.position.pop(0)  # update tail segment (i.e. don't grow) if snake has not eaten
        return (False)

    def set_direction(self, new_direction):
        if not self.direction_received:
            if (abs(new_direction[0]) != abs(self.direction[0]) or  # No 180 degree turns
                abs(new_direction[1]) != abs(self.direction[1])):
                self.direction = new_direction
        else:
            self.direction_buffer = new_direction
        self.direction_received = True

class Food:
    def __init__(self):
        x = random.randrange(CANVAS_WIDTH / CANVAS_RES) * CANVAS_RES
        y = random.randrange(CANVAS_HEIGHT / CANVAS_RES) * CANVAS_RES
        self.position = (x, y)
        self.fill = "#00FF00"
        self.outline = "#000000"

    def update_position(self, snake):
        position_found = False
        while not position_found:
            x_new = random.randrange(CANVAS_WIDTH / CANVAS_RES) * CANVAS_RES
            y_new = random.randrange(CANVAS_HEIGHT / CANVAS_RES) * CANVAS_RES
            position_new = (x_new, y_new)
            if position_new not in snake.position:
                position_found = True
        self.position = position_new


class SnakeGame(tk.Canvas):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind_all("<Key>", self.key_controls)
        self.game_over = False
        self.score = 0
        self.snake = Snake()
        self.food = Food()
        self.refresh = 200  # Refresh board every 200 ms initially

    def draw_food(self):
        x0, y0 = self.food.position
        self.create_rectangle(x0, y0, x0 + CANVAS_RES, y0 + CANVAS_RES,
                              fill=self.food.fill,
                              outline=self.food.outline)

    def draw_snake(self):
        for x0, y0 in self.snake.position[:-1]:
            self.create_rectangle(x0, y0, x0 + CANVAS_RES, y0 + CANVAS_RES,
                                  fill=self.snake.fill_body,
                                  outline=self.snake.outline)

        x_head, y_head = self.snake.position[-1]
        self.create_rectangle(x_head, y_head, x_head + CANVAS_RES, y_head + CANVAS_RES,
                              fill=self.snake.fill_head,
                              outline=self.snake.outline)


    def check_food(self):
        return self.snake.position[-1] == self.food.position

    def key_controls(self, e):
        key = e.keysym
        keymap = {'Left': (-1, 0),
                  'Right': (1, 0),
                  'Up': (0, -1),
                  'Down': (0, 1)}
        if key in keymap:
            self.snake.set_direction(keymap[key])

    def timestep(self):
        # Check if snake collided with itself
        self.game_over = self.snake.move(self.food)
        self.snake.direction_received = False

        # If not, update game state
        if not self.game_over:
            self.delete(tk.ALL)
            # Check if food has been eaten
            food_eaten = self.check_food()
            if food_eaten:
                self.score += 100
                self.food.update_position(self.snake)      # Put food to new position
                self.refresh = int(self.refresh ** 0.997)  # Increase speed

            # Update direction from buffer
            if not self.snake.direction_buffer == None:
                self.snake.set_direction(self.snake.direction_buffer)
                self.snake.direction_buffer = None
            self.draw_food()
            self.draw_snake()
            self.pack()
            self.after(self.refresh, self.timestep)
        # Else: Show Game over screen and score
        else:
            self.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2.5, font="Times 20 bold", text="Game over!")
            self.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, font="Times 16 italic", text="Score: " + str(self.score))

def main():
    # Set up Canvas
    root = tk.Tk()
    root.title('Snake Game')
    root.resizable(width=False, height=False)

    # Initialize Game and run mainloop
    board = SnakeGame(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    board.timestep()
    root.mainloop()

if __name__ == '__main__':
    main()