'''
All code relating to the GUI is stored here
'''
import tkinter as tk
import tkinter.font as font
import SSFunctional as ssf

def Sudoku_Begins():
    
    root = tk.Tk()
    root.title('Sudoku Solver')
    root.geometry('450x500')
    root.resizable(False,False)
    
    ##CREATE WIDGETS
    
    #Creating the Board
    Board = tk.Canvas(root, bg="white", height=450, width=450)   
        #Vertical Lines
    for num in range(9):
        Board.create_line(num*50, 0, num*50, 450, width = ssf.Thickness(num))
        #Horizontal Lines
    for num in range(9):
        Board.create_line(0, num*50, 450, num*50, width = ssf.Thickness(num))
    
    #Create the cell entry array (ssf line 32)
    entry_list = ssf.Entry_Array(root)
    
    #Create the Solve Button
    Buttonfont = font.Font(size = 12,family = "Helvetica")
    Button = tk.Button(root,text="Solve",
                             bg = "white",
                             font = Buttonfont, 
                             command = lambda: ssf.Solve_Button(entry_list))
    
    ##PLACE WIDGETS
    
    Board.place(x=0,y=0)
    Button.place(relx = 0.05, rely = 0.92)
    #place all the entry cells
    
    for i in range(len(entry_list)):
        for j in range(len(entry_list[0])):
            entry_list[i][j].place(x=j*50+5,y=i*50+5,height = 40, width=40)
    
    
    #EVENT LOOP
    root.mainloop()
    
def Sudoku_Solution(solved_puzzle):
    
    root2 = tk.Tk()
    root2.title('Solution!!')
    root2.geometry('450x450')
    root2.resizable(False,False)
    
    ##CREATE WIDGETS
    
    #Creating the Board
    Board = tk.Canvas(root2, bg="white", height=450, width=450)   
        #Vertical Lines
    for num in range(9):
        Board.create_line(num*50, 0, num*50, 450, width = ssf.Thickness(num))
        #Horizontal Lines
    for num in range(9):
        Board.create_line(0, num*50, 450, num*50, width = ssf.Thickness(num))
    
    #Create the label array
    label_list = ssf.Label_Array(root2,solved_puzzle)
    
    ##PLACE WIDGETS
    Board.place(x=0,y=0)
    
    for i in range(len(label_list)):
        for j in range(len(label_list[0])):
            label_list[i][j].place(x=j*50+5,y=i*50+5,height = 40, width=40)
    

    #EVENT LOOP
    root2.mainloop()

if __name__=='__main__':
    Sudoku_Begins()