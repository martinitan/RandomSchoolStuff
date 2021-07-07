
#
# Sudoku Solver
# Purpose is to solve sudoku puzzles
#
#
#
# proposed solution:
# solve by rows
# then solve by columns
# then solve by 3x3 square, This needs to solve implicit positions
# then solve by implicit blocks(2 jumps)
# repeat until no more possible values can be filled in 
#
# if the puzzle is not completed at this point, brute force will be used to complete the puzzle
#


# variables
size = 9
sudoku = [[0,0,0,0,0,0,0,8,0],
		  [6,8,0,4,7,0,0,2,0],
		  [0,1,9,5,0,8,6,4,7],
		  [0,6,0,9,0,0,0,0,4],
		  [3,4,2,6,8,0,0,0,0],
		  [1,9,0,0,5,0,8,3,0],
		  [0,0,0,7,2,6,4,0,3],
		  [0,0,6,0,0,5,0,1,0],
		  [0,0,3,8,9,1,5,0,0]] #puzzle to be solved. arraged as sudoku[row][column]. 0 indicates an empty spot


#
#  ------------------- 
#  |  1  |  2  |  3  |
#  ------------------- 
#  |  4  |  5  |  6  |
#  ------------------- 
#  |  7  |  8  |  9  |
#  -------------------
#
# row, column
regions = {1:[0,0], 2:[0,3], 3:[0,6], 4:[3,0], 5:[3,3], 6:[3,6], 7:[6,0], 8:[6,3], 9:[6,6]}



def printSudoku():
	global sudoku
	print("|-----------------------------|")
	for i in range(0,9):
		print("| " + str(sudoku[i][0]) + "  " + str(sudoku[i][1]) + "  " + str(sudoku[i][2]) + " | " + str(sudoku[i][3]) + "  " + str(sudoku[i][4])
		+ "  "+ str(sudoku[i][5])+ " | " + str(sudoku[i][6]) + "  " + str(sudoku[i][7]) + "  " + str(sudoku[i][8])+ " |")
		if(i%3 == 2):
			print("|-----------------------------|")
	

#
# returns which region a particular tile is in
#
def getRegion(Srow, Scolumn):
	for region, coord in regions.items():
		row, column = coord
		if((( Srow == row ) or (Srow == row+1) or (Srow == row+2)) 
		and (( Scolumn == column) or (Scolumn == column+1) or (Scolumn == +2))) :
			return region
			
#
# solves a row with one missing value. 
#
# input is actual row number, 1-9 inclusive
#
def solveRow(rowNumber):
	global sudoku
	numMissing = 0
	valueMissing = ['nothing here', 'yes','yes','yes','yes','yes','yes','yes','yes','yes']
	spot = 0

	
	for x in range(0,9):
		if(sudoku[rowNumber-1][x] == 0):
			numMissing += 1
			spot = x
		else:
			valueMissing[sudoku[rowNumber-1][x]] = 'no'
	if(numMissing == 1):
		sudoku[rowNumber-1][spot] = valueMissing.index('yes')
		return True
	return False

#
# used to test solveRow
# when test is failed, output the puzzle to observe failure
#
def testSolveRow():
	global sudoku
	print("Solving Rows Test")
	sudoku = [[1,2,3,4,5,6,7,8,0],
		  [2,0,1,3,4,5,6,9,7],
		  [3,6,7,0,9,2,1,4,5],
		  [4,2,1,3,5,6,7,0,0],
		  [5,0,0,0,0,0,0,0,0],
		  [6,7,8,9,1,2,3,4,5],
		  [7,8,9,1,2,4,3,5,0],
		  [8,9,1,2,3,4,0,6,7],
		  [9,1,2,3,4,5,6,7,0]]
	solveRow(1)
	if(sudoku[0][8] != 9):
		printSudoku()
		print("Failed 1")
	else:
		print("Passed 1")
	solveRow(2)
	if(sudoku[1][1] != 8):
		printSudoku()
		print("Failed 2")
	else:
		print("Passed 2")
	solveRow(3)
	if(sudoku[2][3] != 8):
		printSudoku()
		print("Failed 3")
	else:
		print("Passed 3")
	solveRow(4)
	if((sudoku[3][8] != 0) and (sudoku[4][7] != 0)):
		printSudoku()
		print("Failed 4")
	else:
		print("Passed 4")
	solveRow(5)
	if((sudoku[4][8] != 0) and (sudoku[4][1] != 0)and (sudoku[4][2] != 0)and (sudoku[4][3] != 0)and (sudoku[4][4] != 0)and (sudoku[4][5] != 0)and (sudoku[4][6] != 0)and (sudoku[4][7] != 0)):
		printSudoku()
		print("Failed 5")
	else:
		print("Passed 5")
	result=solveRow(6)
	if(result != False):
		printSudoku()
		print("Failed 6")
	else:
		print("Passed 6")
	solveRow(7)
	if(sudoku[6][8] != 6):
		printSudoku()
		print("Failed 7")
	else:
		print("Passed 7")
	solveRow(8)
	if(sudoku[7][6] != 5):
		printSudoku()
		print("Failed 8")
	else:
		print("Passed 8")
	solveRow(9)
	if(sudoku[8][8] != 8):
		printSudoku()
		print("Failed 9")
	else:
		print("Passed 9")
	print("Test Complete")


#
# solves a column with one missing value. 
#
# input is actual column number, 1-9 inclusive
# 	
def solveColumn(columnNumber):
	global sudoku
	numMissing = 0
	valueMissing = ['nothing here', 'yes','yes','yes','yes','yes','yes','yes','yes','yes']
	spot = 0

	
	for x in range(0,9):
		if(sudoku[x][columnNumber-1] == 0):
			numMissing += 1
			spot = x
		else:
			valueMissing[sudoku[x][columnNumber-1]] = 'no'
	if(numMissing == 1):
		sudoku[spot][columnNumber-1] = valueMissing.index('yes')
		return True
	return False
	

#
# used to test solveColumn
# when test is failed, output the puzzle to observe failure
#
def testSolveColumn():
	global sudoku
	print("Solving Columns Test")
	sudoku = [[1,2,3,4,5,6,7,1,1],
		      [2,0,4,3,0,5,6,2,2],
		      [3,4,0,0,0,4,1,3,3],
		      [4,5,6,0,0,3,8,4,4],
		      [5,6,7,5,0,2,5,8,5],
		      [6,7,8,9,0,1,4,6,6],
		      [7,8,9,1,0,9,0,7,7],
		      [8,9,1,2,0,8,3,0,9],
		      [9,1,2,3,0,7,2,9,0]]
	result = solveColumn(1)
	if(result != False):
		printSudoku()
		print("Failed 1")
	else:
		print("Passed 1")
	solveColumn(2)
	if(sudoku[1][1] != 3):
		printSudoku()
		print("Failed 2")
	else:
		print("Passed 2")
	solveColumn(3)
	if(sudoku[2][2] != 5):
		printSudoku()
		print("Failed 3")
	else:
		print("Passed 3")
	solveColumn(4)
	if((sudoku[3][3] != 0) and (sudoku[4][3] != 0)):
		printSudoku()
		print("Failed 4")
	else:
		print("Passed 4")
	solveColumn(5)
	if((sudoku[1][4] != 0) and (sudoku[2][4] != 0)and (sudoku[3][4] != 0)and (sudoku[4][4] != 0)and (sudoku[5][4] != 0)and (sudoku[6][4] != 0)and (sudoku[7][4] != 0)and (sudoku[8][4] != 0)):
		printSudoku()
		print("Failed 5")
	else:
		print("Passed 5")
	result=solveColumn(6)
	if(result != False):
		printSudoku()
		print("Failed 6")
	else:
		print("Passed 6")
	solveColumn(7)
	if(sudoku[6][6] != 9):
		printSudoku()
		print("Failed 7")
	else:
		print("Passed 7")
	solveColumn(8)
	if(sudoku[7][7] != 5):
		printSudoku()
		print("Failed 8")
	else:
		print("Passed 8")
	solveColumn(9)
	if(sudoku[8][8] != 8):
		printSudoku()
		print("Failed 9")
	else:
		print("Passed 9")
	print("Test Complete")

	
#
# checks a row for a value, if the value is present the position is returned
# otherwise -1 is returned
#
def valueInRow(rowNumber, Value):
	global sudoku
	for x in range(0,9):
		if(sudoku[rowNumber-1][x] == Value):
			return x
	return -1
		
	
#
# checks a column for a value, if the value is present the position is returned
# otherwise -1 is returned
#
def valueInColumn(columnNumber, Value):
	global sudoku
	for x in range(0,9):
		if(sudoku[x][columnNumber-1] == Value):
			return x
	return -1

	
	
def valueInRegion(region, Value):
	global sudoku
	row,column = regions.get(region)
	for x in range(0,3):
		for y in range(0,3):
			if(sudoku[row+x][column+y] == Value):
				return Value
	return -1
#
#
# this version currently requires 2 columns and 2 rows to be filled with a value 
# before being able to solve for the value in the 3x3
#
#

def solve3x3(regionNumber, Value):
	rows = []
	columns = []
	rCount = 0
	cCount = 0
	global sudoku
#check if value is already in region	
	if(valueInRegion(regionNumber,Value) != -1):
		return
#first convert region to 3x3 coords
	row,column = regions.get(regionNumber)
#check if value is in a row or column, and record which rows and columns
	for x in range(1,4): # 1,2,3
		if(valueInRow(row + x,Value) != -1): #if value is in row
			rows.append(x)                   #record the row number
			rCount +=1                       #increase the count of rows with the value in it
		else:
			rows.append(-1)
		if(valueInColumn(column + x,Value) != -1):
			columns.append(x)
			cCount += 1
		else:
			columns.append(-1)
	#if exactly 2 rows and 2 columns have the value in it, fill the row and column that doesnt have the value with the value.
	if(rCount == 2 and cCount == 2):
		for x in range(0,3):
			if(rows[x] == -1):
				for y in range(0,3):
					if(columns[y] == -1):
						sudoku[row + x][column + y] = Value
						return Value
	return -1	

#
# determines if a value is in a row implicitly. The value must be in certain spots in the row thereby making the vaule unable to be in other spots
#
# example :
#            | 1 2 3 | 4 5 6 | 7 8 9 |
#            | 4 5 6 |(7 8 9)|(1 2 3)|
#            |(7 8 9)|(1 2 3)|(4 5 6)|
#                      
#            the values in () are implicit
# 
# returns           0 if value in row 
#                   -1 otherwise
def valueInRowImplicit(RegionNumber, RowNumber, value):
	#check if value in row
	if(valueInRow(rowNumber,value)):
		return 0
	#check value in other rows in the region 
	Rrow, Rcolumn = regions.get(RegionNumber)
	#
	
	return -1

def valueInColumnImplicit(RegionNumber, ColumnNumber, value):
	return -1
	
	
#def bruteForceSudoku(SU[][]):
#	for x in range(0,9):
#		for y in range(0,9):
#			if(sudoku[x][y] == 0):
#				bruteForeceSudoku(SU[][])
	
#S	return
	
	
def testSolve3x3():
	global sudoku
	print("Solving 3x3 Test")
	sudoku = [[0,0,0,0,0,0,0,0,2],
		      [0,0,0,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,2],
		      [2,0,2,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,0],
		      [0,0,0,0,0,0,0,0,0]]
	print(valueInColumn(0,2))
	
	solve3x3(1,2)
	printSudoku();
	
def solveSudoku():
	for y in range(0,100):
		for x in range(1,10):
			solveRow(x)
		for x in range(1,10):
			solveColumn(x)
		for x in range(1,10):
			for y in range(1,10):
				solve3x3(x,y)
				
printSudoku()
print('\n')
solveSudoku()
printSudoku()
	
	
	

