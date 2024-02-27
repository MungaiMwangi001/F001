class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            # store the elements of a single row in the sudoku board.
            row_list = []
            #split each row in three segments, in order to represent the 3x3 squares properly
            #slicing to create the three lists of equal length representing the line segment of each 3x3 square 
            #enumeration starts from 1 instead of 0
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                #string representation of the row with spaces between each element
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty
            
            #want to handle the last row differently.
            if index < 8:
                 #verify if the row is the last row inside a 3x3 square.
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                #handle the last row of the entire board
                board_string += lower_lines
        #string contains the complete visual representation of the sudoku board
        return board_string

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                #find the index of the first occurrence of 0 in the current row
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None
    
    #checks if a given number can be inserted into a specified row of the sudoku board
    def valid_in_row(self, row, num):
        return num not in self.board[row]
     
     #hecks if a number can be inserted in a specified column 
    def valid_in_col(self, col, num):
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row, col, num):
        #calculate the starting row index for the 3x3 block in the board grid
        row_start = (row // 3) * 3
        #calculate the starting column index for the 3x3 block in the board grid
        col_start=(col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            #iterate over a sequence of three element
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
                #If the number is not present, it can be inserted into the square 
        return True
    '''
empty (a tuple representing the row and column indices of an empty cell)
num (representing the number to be checked).
'''
    #checks if a given number is a valid choice for an empty cell
    def is_valid(self, empty, num):
        row, col = empty
        #Check if the number is valid for insertion in the specified row
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

#attempts to solve the sudoku in-place
    def solver(self):
        #walrus operator (:=) combine the assignment and the conditional check into a single line 
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    #recursively call the  function to solve the rest of the sudoku
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

#create a function to print and solve the sudoku board.
def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)

    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard
puzzle = [
  [9, 0, 0, 6, 7, 0, 0, 0, 0],
  [2, 0, 0, 9, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 6, 2, 0],
  [0, 5, 0, 0, 1, 0, 8, 0, 6],
  [0, 1, 0, 0, 0, 3, 0, 0, 7],
  [0, 0, 0, 0, 2, 0, 0, 0, 0],
  [0, 0, 5, 7, 0, 0, 0, 0, 3],
  [0, 0, 9, 0, 0, 4, 0, 0, 8],
  [0, 0, 0, 0, 0, 0, 1, 5, 2]
]
solve_sudoku(puzzle)


'''
A new instance of a class is created by using the function notation: ClassName(). The instantiation creates
 an empty object. Classes can have methods, which are like local functions for each instance.
The __init__ method is a special method that allows you to instantiate an object to a customized state. 
When a class implements an __init__ method, __init__ is automatically called upon instantiation.

Add two parameters to the __init__ method, order matters:
self: This is a reference to the instance of the class. It is a convention to name this parameter self.
board: The board parameter is expected to be passed when creating an instance of the Board class.

Define a method __str__ within the Board class. Also, add the self parameter. 
This method is automatically called when you use the str() function on 
an instance of the class or when you use print() with the object.

The enumerate() function is a built-in function in Python that takes an iterable (such as a list, tuple,
 or string) and returns an iterator that produces tuples containing indices and corresponding values from the iterable.
'''