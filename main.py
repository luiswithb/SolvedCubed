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

def main():
    # test() will only print if there is an error, the output without errors should only be
    # the initial cube and the ending state
    test() 

    scramble()
    print("Scrambled cube:")
    printCube()

    cross()
    corners()
    middleLayer()

    print("Ending cube:")
    printCube()

    #print(solutionMoves)

if __name__ == "__main__":
    main()