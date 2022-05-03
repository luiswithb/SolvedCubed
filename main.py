from pickletools import optimize
from solver import *

def test():
    for i in range(100):
        scramble()
        cross()
        cubeM = deepcopy(cube)
        corners()
        middleLayer()

        if((cross()) and (corners()) and (middleLayer())): pass
        else:
            for i in cubeM:
                print(i)
            print('-'*60)
            
        resetCube()

def resetCube():
    cube = deepcopy(solvedCube)

def solution():
    temp = []
    for i in solutionMoves:
        temp.append(i.__name__)
    return temp

def threeInRow(s):
    t = []

    i = 0
    while i < len(s) - 2:
        if (s[i] == s[i+1]) and (s[i+1] == s[i+2]):
            t.append(s[i] + 'i')
            i += 3
        else:
            t.append(s[i])
            i += 1

    return t

def optimize(s):
    t = []

    i = 0
    while i < len(s) - 2:
        if((len(s[i]) == 2) and (s[i+1] == s[i][0])):
            i += 2
        else:
            t.append(s[i])
            i += 1

        if((len(s[i]) == 2) and (s[i+1] == s[i][0])):
            i += 2
        else:
            t.append(s[i])
            i +=1

    return t

def main():
    print("Scrambled cube:")
    s = scramble()
    printCube()
    print("Scramble moves:",s)

    cross()
    corners()
    middleLayer()
    while not orientLastLayer():
        movesInBlueOrientation("F U R Ui Ri Fi") # algorithm to get a differnt orientation of the yellow layer
    p = permuteLastLayer()

    # performs an algorithm that gets a different permutation in case the permutation is one of the ones not implemented yet
    # runs until it finds one that has been implemented
    while not p:
        Ri()
        U()
        Ri()
        D2()
        R()
        Ui()
        Ri()
        D2()
        R2()
        p = permuteLastLayer()

    # last layer is solved but sometimes not oriented properly, this fixes that
    if p:
        while(cube != solvedCube):
            movesInBlueOrientation("U")

    print("Ending cube:")
    printCube()
    solutionMoves = solution()
    solutionMovesO = threeInRow(solutionMoves)
    solutionMovesFinal = optimize(solutionMovesO)

    if cube == solvedCube:
        print("Solved!")
        print("Solution moves:",solutionMovesFinal)
        print("Number of moves:", len(solutionMovesFinal))
        print("-----------------------------")
        print(solutionMoves)
        print(len(solutionMoves))
    else:
        print("Could not solve :(")
        return False

if __name__ == "__main__":
    main()