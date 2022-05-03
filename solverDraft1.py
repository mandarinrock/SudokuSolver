import sys, getopt # DELETE second

# def printInput(inputArguments):

#     print('arguments: ', inputArguments)



def loadPuzzle(puzzlePath):

    with open(puzzlePath, "r") as puzzleFile:

        originalPuzzle = puzzleFile.readlines()

    for i in range(len(originalPuzzle)):

        # originalPuzzle[i].split()
        print(originalPuzzle[i], end = "")

        # for j in range(len(originalPuzzle[i])):

            # print(originalPuzzle[i][j], end= " ")


def sudokuSolver():

    if len(sys.argv) != 2:

        # print('arguments: ', sys.argv) # DEBUG
        userInput = input("Please enter path to puzzle file: ")
        loadPuzzle(userInput)

    else:

        loadPuzzle(sys.argv[1])



def main():

    # printInput(sys.argv)
    sudokuSolver()


if(__name__ == '__main__'):
    main()