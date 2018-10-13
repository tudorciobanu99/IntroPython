import numpy as np
def fillSudokuRow(sudokuRow):
    A = 0
    for i in range(0, len(sudokuRow)):
        if (sudokuRow[i] == 0):
            A = i
    for j in range(1,10):
        if (j not in sudokuRow):
            sudokuRow[A] = j
    return sudokuRow