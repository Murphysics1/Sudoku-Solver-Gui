'''
All classes and functions for the Sudoku Solver 

'''
import tkinter as tk
import SSGUI as ssgui


def Thickness(num):
    '''
    Parameters
    ----------
    num : int
        Either the row or column number

    Returns
    -------
    int
        The return is the thickness of the line thick(4) or thin (1) depending on whether the row or column mod(3) = 0
    '''
    
    if num%3 == 0:
        return 4
    else:
        return 1


def Entry_Array(master):
    '''
    Parameters
    ----------
    master : tkinter call
        Which instance of the tkinter class 

    Returns
    -------
    entry_list : array
        Returns an array of entry objects with for the sudoku board

    '''
    entry_list = []
    rows_list = []
    
    for i in range(9):
        for j in range(9):
            rows_list.append(tk.Entry(master,
                                      justify = 'center',
                                      relief = 'flat',
                                      font=('Helvetica',20)))
        entry_list.append(rows_list)
        rows_list = []
    
    return entry_list

def Valid_Input(guess,loc,grid_space):
    '''
    Checks to see is a guess is valid
    
    Parameters
    ----------
    guess : int
        The number that is being tried
    loc : tuple
        Location is a tuple of (row,column)
    grid_space : array
        The Sudoku puzzle

    Returns
    -------
    bool
        Return true if the guess a valid number for the location
    '''
    
    
    # loc is a tuple returned from the zero_loc function
    # row id-> loc[0] ; column id -> loc[1]
    
    # check row
    for num in range(len(grid_space)):
        if guess == grid_space[loc[0]][num]:
            return False
    
    # check column
    for num in range(len(grid_space[0])):
        if guess == grid_space[num][loc[1]]:
            return False
        
    # check square
    # I dont like the square check, there should be a cleaner way, but it works
    # this will slow down the algorithm
    subsquare_elements =[]
    
    # creates the list for the items in each subsquare
    # map is above 
    for row in range(len(grid_space)):
        if loc[0]//3 == row//3:
            for column in range(len(grid_space[0])):
                if column//3 == loc[1]//3:
                    subsquare_elements.append(grid_space[row][column])
                    
    # if the item is in the list, then it is in the subsquare       
    if guess in subsquare_elements:
        return False
    
    # if its not in the row, column, or susquare, then it is a valid input
    return True

def Zero_Loc(grid_space):
    '''
    Finds the next zero in the grid space

    Parameters
    ----------
    grid_space : array
        the Sudoku puzzle

    Returns
    -------
    location: tuple
        if a zero is found, the location (row,column) is returned
        if a zero is not found, False is returned meaning the puzzle is solved
    '''
    for row in range(len(grid_space)):
        for col in range(len(grid_space[0])):
            if grid_space[row][col] == 0:
                return (row,col)
    
    return False

def Solve(grid_space):
    '''
    Recursively solves the Sudoku puzzle using a backtracking algorith

    Parameters
    ----------
    grid_space : array
        the Sudoku puzzle

    Returns
    -------
    bool
       True - Puzzle is solved

    '''
    # if there are no zeros:
    if Zero_Loc(grid_space) == False:
        # then the puzzle is soved
        return True
    
    # otherwise, move into the solving algorithm
    else:
        # unpack the tuple
        row,col = Zero_Loc(grid_space)
        # start trying #1-9
        for guess in range(1,len(grid_space)+1):
            if Valid_Input(guess,(row,col),grid_space):
                # if a valid number is found, replace it in the grid
                grid_space[row][col] = guess
                
                # call this function again and see if the problem is solvable
                if Solve(grid_space):
                    return True
                
                # if not then reset and move onto the next value in the guess for loop
                grid_space[row][col] = 0

def Label_Array(master,solved_puzzle):
    '''
    Generate an array of label objects for the solved puzzle

    Parameters
    ----------
    master : tkinter call
        
    solved_puzzle : array
        

    Returns
    -------
    Labels : array
        An array of label objects

    '''
    Labels = []
    Label_Rows = []
    
    for i in range(9):
        for j in range(9):
            Label_Rows.append(tk.Label(master,
                                      text = f'{solved_puzzle[i][j]}',
                                      justify = 'center',
                                      bg = 'white',
                                      relief = 'flat',
                                      font=('Helvetica',20)))
        Labels.append(Label_Rows)
        Label_Rows = []
    
    return Labels

def Solve_Button(entry_list):
    '''
    Functionality of the Solve button. Returns a solved grid in a separate window

    Parameters
    ----------
    entry_list : array, str 
        User input of the Sudoku puzzle

    Returns
    -------
    None

    '''
    
    puzzle =[]
    puzzle_row = []
    
    # convert all entry fields into an array that the sudoku solver can use
    for i in range(9):
        for j in range(9):
            x = entry_list[i][j].get()
            if x == '':
                puzzle_row.append(0)
            else:
                puzzle_row.append(int(x))
        puzzle.append(puzzle_row)
        puzzle_row = []
    
    Solve(puzzle)
    
    ssgui.Sudoku_Solution(puzzle)
