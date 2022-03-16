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

def main():
    # test() will only print if there is an error, the output without errors should only be
    # the initial cube and the ending state
    test() 

    print("Scrambled cube:")
    s = scramble()
    printCube()
    print("Scramble moves:",s)

    cross()
    corners()
    middleLayer()
    while not orientLastLayer():
        movesInBlueOrientation("F U R Ui Ri Fi") # algorithm to get a differnt orientation of the yellow layer

    print("Ending cube:")
    printCube()

    #print(solutionMoves)

if __name__ == "__main__":
    main()