import numpy as np
import copy


class Board:
    def __init__(self, board_size):
        self.grid = np.zeros(shape=(board_size, board_size))
        self.length = board_size
        self.live_amount = 0
        self.age = 0
        self.most_lives_so_far = 0
        self.most_lived_age = 0
        self.most_lived_grid = np.zeros(shape=(board_size, board_size))
        self.initial_live_cells = 0

    def init_cell(self, x_index, y_index, value):
        if self.grid[x_index][y_index] > value:
            self.live_amount -= 1
        elif self.grid[x_index][y_index] < value:
            self.live_amount += 1
        self.grid[x_index][y_index] = value

    def get_cell_value(self, x_index, y_index):
        return self.grid[x_index][y_index]

    def get_live_neighbors(self, x_index, y_index):
        # gets cell by it's indexes and returns an array of tuples of indexes of it's live neighbors
        arr = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x_index + i < self.length:
                    if 0 <= y_index + j < self.length:
                        if self.grid[x_index+i][y_index+j] == 1:
                            arr.append((x_index + i, y_index + j))
        if self.grid[x_index][y_index] == 1:
            arr.remove((x_index, y_index))
        return arr

    def get_next_cell_state(self, x_index, y_index):
        live_neighbors = len(self.get_live_neighbors(x_index, y_index))
        if self.grid[x_index][y_index] == 1:  # it's a live cell
            if 2 <= live_neighbors <= 3:
                return 1
            else:
                self.live_amount -= 1
                return 0
        else:  # it's a dead cell
            if live_neighbors == 3:
                self.live_amount += 1
                return 1
            else:
                return 0

    def next_generation(self):
        new_board = copy.deepcopy(self.grid)
        for i in range(self.length):
            for j in range(self.length):
                cell_state = self.get_next_cell_state(i, j)
                new_board[i][j] = cell_state

        # eliminates useless calculations when reached a static state
        if np.array_equal(self.grid, new_board):
            return False

        self.grid = new_board
        if self.most_lives_so_far < self.live_amount:
            self.most_lives_so_far = self.live_amount
            self.most_lived_age = self.age
            self.most_lived_grid = copy.deepcopy(self.grid)

        self.age += 1
        return True

    def next_amount_of_generations(self, amount: int):
        for i in range(amount):
            if not self.next_generation():
                self.age += (amount - i)
                break

    def __str__(self):
        return f'the board has the following properties:\n' \
               f'size length: {self.length}\n' \
               f'initial live amount: {self.initial_live_cells}\n' \
               f'current age: {self.age}\n' \
               f'current live amount: {self.live_amount}\n' \
               f'most lives so far: {self.most_lives_so_far}\n' \
               f'most lives was in age: {self.most_lived_age}\n'

    def is_valid_meth_board(self):
        # takes a board of initial methuselah
        # make  sure it has at least 4 living cells and no more than 15
        if self.initial_live_cells < 4 or self.initial_live_cells > 15:
            return False

        self.next_amount_of_generations(self.length)
        # need to make sure it's not static, or oscillator until age 30 or more
        grid_after_gen__amount = self.grid
        for i in range(20):
            self.next_generation()
            if np.array_equal(self.grid, grid_after_gen__amount):
                # means that the methuselah live less than 30 generation until convergence to static/oscillator
                return False

        self.next_amount_of_generations(100 - self.age)
        return True

    def copy_board(self):
        return copy.deepcopy(self)

    @staticmethod
    def create_board_from_methuselah(size, methuselah):
        # gets 5X5 methuselah numpy array and enters it to size X size array on top left
        board = Board(size)
        board.grid = expand_array(methuselah, size)
        board.live_amount = np.sum(board.grid)
        board.initial_live_cells = board.live_amount
        board.most_lives_so_far = board.live_amount
        return board


def expand_array(arr, new_size):
    result = np.zeros((new_size, new_size))
    result[:arr.shape[0],:arr.shape[1]] = arr
    return result


def grade_methuselah(methuselah: Board):
    return methuselah.most_lives_so_far / methuselah.initial_live_cells
