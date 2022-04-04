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

    if cube == solvedCube:
        print("Solved!")
        print("Solution moves:",solution())
        print("Number of moves:", len(solution()))
        return solution()
    else:
        print("Could not solve :(")
        return False

if __name__ == "__main__":
    main()