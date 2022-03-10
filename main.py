from solver import *

def test():
    for i in range(100):
        scramble()
        cross()
        corners()

        if((not corners()) or (not cross())):
            printCube()

def main():
    #test()

    scramble()
    printCube()
    cross()
    corners()
    middleLayer()
    printCube()
    
    print(solutionMoves)

if __name__ == "__main__":
    main()