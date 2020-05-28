import subprocess

class QueenChessBoard:
    def __init__(self, size):
        
        self.size = size
        
        self.columns = []
 
    def get_size(self):
        return self.size
 
    def get_queens_count(self):
        return len(self.columns)
 
    def place_in_next_row(self, column):
        self.columns.append(column)
 
    def remove_in_current_row(self):
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column):
        
        row = len(self.columns)
 
        
        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
      
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
 
    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('1', end=' ') #queen
                else:
                    print('0', end=' ') #blank tile
            print()
 
 
def print_all_solutions_to_n_queen(size):
    
    board = QueenChessBoard(size)
    number_of_solutions = print_all_solutions_helper(board)
    print('Arithmos Lysewn:', number_of_solutions)
 
def print_all_solutions_helper(board):
    
    size = board.get_size()
 
    
    if size == board.get_queens_count():
        board.display()
        print()
        return 1
 
    number_of_solutions = 0
    
    for column in range(size):
        if board.is_this_column_safe_in_next_row(column):
            board.place_in_next_row(column)
            number_of_solutions += print_all_solutions_helper(board)
            board.remove_in_current_row()
 
    return number_of_solutions
 
 
n = int(input('Dwse n: \n'))
print_all_solutions_to_n_queen(n)