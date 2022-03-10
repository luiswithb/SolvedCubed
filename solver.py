from cube import *
import random

solvedCube = [['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
              ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
              ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
              ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
              ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_'],
              ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_']]

moves = [R,L,U,D,F,B]# R2,L2,U2,D2,F2,B2,Ri,Li,Ui,Di,Di,Fi,Bi]

def scramble():
    for i in range(20):
        r = random.randint(0,len(moves) - 1)
        moves[r]()
    solutionMoves.clear()

def printCube():
    for x in cube:
        print(x)
    print("\n")

# 12 edge pieces, numerated as follows:
# FRONT LAYER, white face
#     1
#  4  w  2
#     3

# MIDDLE LAYER
#   8    5
#
#   7    6

# BACK LAYER
#     9
#  12   10
#     11
edgeLinks = [
                [[2, 4], [3, 4]], # 1
                [[4, 5], [4, 6]], # 2
                [[5, 4], [6, 4]], # 3
                [[4, 2], [4, 3]], # 4

                [[1, 5], [3, 7]], # 5
                [[5, 7], [7, 5]], # 6
                [[5, 1], [7, 3]], # 7
                [[1, 3],[3, 1]], # 8

                [[0, 4], [3, 10]], # 9
                [[4, 8], [4, 9]], # 10
                [[5, 10], [8, 4]], # 11
                [[4, 0], [4, 11]], # 12
            ]

# colors of the edges, position does not matter when stored but it does when checking the edge orientation
# may not need
edgeColors =    [
                    ['b','o'],
                    ['b', 'r'],
                    ['b', 'y'],
                    ['y', 'g'],
                    ['r', 'g'],
                    ['o', 'g'],
                    ['o', 'w'],
                    ['o', 'y'],
                    ['b', 'w'],
                    ['w', 'r'],
                    ['w', 'g'],
                    ['r', 'y']
                ]
# 8 corner pieces, numerated as follows:
# FRONT LAYER, white face
#   4   1
#     w
#   3   2

# BACK LAYER
#   8   5
#     
#   7   6
cornerLinks =   [
                    [[3,5],[2,5],[3,6]], #1
                    [[5,5],[5,6],[6,5]], #2
                    [[5,3],[6,3],[5,2]], #3
                    [[3,3],[3,2],[2,3]], #4

                    [[3,9],[0,5],[3,8]], #5
                    [[5,9],[5,8],[8,5]], #6
                    [[5,11],[8,3],[5,0]], #7
                    [[3,11],[3,0],[0,3]], #8
                ]

# colors of the corners, position does not matter when stored but it does when checking the corner orientation
# may not need
cornerColors =  [
                    ['w','b','r'],
                    ['w','r','g'],
                    ['w','g','o'],
                    ['w','o','b'],

                    ['y','b','r'],
                    ['y','r','g'],
                    ['y','g','o'],
                    ['y','o','b'],
                ]

# returns the edge's coordinates based on the edges colors, a and b
def getEdgePos(a,b):
    for x in edgeLinks:
        if (a == cube[x[0][0]][x[0][1]] and b == cube[x[1][0]][x[1][1]]) or (b == cube[x[0][0]][x[0][1]] and a == cube[x[1][0]][x[1][1]]):
            return x

# getEdgeNum returns the value of the edge
def getEdgeNum(ePos):
    for i in range(len(edgeLinks)):
        if ePos == edgeLinks[i]:
            return i + 1

# performs specific moves based on the edge's position and orientation
def edgeToCorrectPos(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)
    if edgeNum == 1:
        if cube[edgePos[0][0]][edgePos[0][1]] != c2:
            U()
            Fi()
            L()
            F()
    elif edgeNum == 2:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            R()
            U()
        else:
            R()
            U()
            F()
            R()
            Fi()
            U()
    elif edgeNum == 3:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            D()
            F()
            R()
            Fi()
        else:
            D()
            F2()
            Di()
            F2()
    elif edgeNum == 4:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Li()
            Fi()
            L()
            F()
        else:
            Li()
            Ui()
    elif edgeNum == 5:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            U()
        else:
            F()
            Ri()
            Fi()
    elif edgeNum == 6:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            F()
            R()
            Fi()
        else:
            F()
            R2()
            Fi()
            U()
    elif edgeNum == 7:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Fi()
            Li()
            F()
        else:
            Fi()
            L2()
            F()
            Ui()
    elif edgeNum == 8:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Ui()
        else:
            Fi()
            L()
            F()
    elif edgeNum == 9:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            U2()
        else:
            U()
            F()
            Ri()
            Fi()
    elif edgeNum == 10:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B()
            U2()
        else:
            B()
            U()
            F()
            Ri()
            Fi()
    elif edgeNum == 11:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B2()
            U()
            F()
            Ri()
            Fi()
        else:
            B2()
            U2()
    elif edgeNum == 12:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Bi()
            U2()
        else:
            Bi()
            Ui()
            Fi()
            L()
            F()

# solves the white cross
def cross():
    a, b, c, d = False, False, False, False
    if((cube[3][4] != cube[4][4]) or (cube[2][4] != cube[1][4])): # top white/blue edge not in place AKA edge #1
        edgeToCorrectPos('w','b')
    # edgeToCorrectPos was written for the white/blue edge, so if we rotate any white/<COLOR> to white/blue's place,
    # then we can perform the same algorithm but just take care of the rotation, 
    # hence the moves before and after the function call in the following if statements.
    else:
        a = True
    if((cube[4][3] != cube[4][4]) or (cube[4][2] != cube[4][1])): # left white/orange edge not in place AKA edge #4
        F() # move white/orange to white/blue's place
        edgeToCorrectPos('w','o')
        Fi() # undo rotation
    else:
        b = True
    if((cube[4][5] != cube[4][4]) or (cube[4][6] != cube[4][7])): # right white/red edge not in place AKA edge #2
        Fi() # move white/red to white/blue's place
        edgeToCorrectPos('w','r')
        F() # undo rotation
    else:
        c = True
    if((cube[5][4] != cube[4][4]) or (cube[6][4] != cube[7][4])): # bottom white/green edge not in place AKA edge #3
        F2() # move white/green to white/blue's place
        edgeToCorrectPos('w','g')
        F2() # undo rotation
    else:
        d = True

    if a and b and c and d: return True
    else: return False

def getCornerPos(a,b,c):
    for x in cornerLinks:
        if (a == cube[x[0][0]][x[0][1]] and b == cube[x[1][0]][x[1][1]] and c == cube[x[2][0]][x[2][1]]) or (a == cube[x[0][0]][x[0][1]] and c == cube[x[1][0]][x[1][1]] and b == cube[x[2][0]][x[2][1]]) or (b == cube[x[0][0]][x[0][1]] and a == cube[x[1][0]][x[1][1]] and c == cube[x[2][0]][x[2][1]]) or (c == cube[x[0][0]][x[0][1]] and a == cube[x[1][0]][x[1][1]] and b == cube[x[2][0]][x[2][1]]) or (c == cube[x[0][0]][x[0][1]] and b == cube[x[1][0]][x[1][1]] and a == cube[x[2][0]][x[2][1]]) or (b == cube[x[0][0]][x[0][1]] and c == cube[x[1][0]][x[1][1]] and a == cube[x[2][0]][x[2][1]]):
            return x

def getCornerNum(cPos):
    for i in range(len(cornerLinks)):
        if cPos == cornerLinks[i]:
            return i + 1

def cornerToCorrectPos(c1,c2,c3):
    cornerPos = getCornerPos(c1,c2,c3)
    cornerNum = getCornerNum(cornerPos)

    if cornerNum == 1:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            R()
            B()
            Ri()
            B2()
            Ui()
            B()
            U()
        else:
            R()
            Bi()
            Ri()
            Ui()
            Bi()
            U()
    elif cornerNum == 2:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            D()
            B()
            Di()
            Ui()
            Bi()
            U() 
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            D()
            Ui()
            B()
            Di()
            U()
        else:
            D()
            B()
            Di()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
    elif cornerNum == 3:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            Di()
            Bi()
            D()
            B2()
            Ui()
            B()
            U()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            Di()
            B()
            D()
            Ui()
            B2()
            U()
        else:
            Di()
            Bi()
            D()
            R()
            Bi()
            Ri()
    elif cornerNum == 4:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            R()
            Li()
            Bi()
            L()
            Ri()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            U()
            Bi()
            Ui()
            Bi()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
        else:
            U()
            Bi()
            Ui()
            Bi()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
    elif cornerNum == 5:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            Ui()
            Bi()
            U()
        else:
            Bi()
            Ui()
            B()
            U()
    elif cornerNum == 6:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            B()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            B()
            Ui()
            Bi()
            U()
        else:
            Ui()
            B()
            U()
    elif cornerNum == 7:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            B2()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            R()
            B2()
            Ri()
        else:
            B()
            Ui()
            B()
            U()
    elif cornerNum == 8:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c1:
            Bi()
            R()
            B2()
            Ri()
            Bi()
            Bi()
            Ui()
            B()
            U()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            R()
            Bi()
            Ri()
        else:
            B2()
            Ui()
            B()
            U()

def corners():
    a, b, c, d = False, False, False, False

    if((cube[3][5] != cube[4][4]) or (cube[2][5] != cube[1][4]) or (cube[3][6] != cube[4][7])): # white/blue/red corner not in place
        cornerToCorrectPos('w','b','r')
    else:
        a = True
    if((cube[5][5] != cube[4][4]) or (cube[5][6] != cube[4][7]) or (cube[6][5] != cube[7][4])): # white/red/green corner not in place
        Fi()
        cornerToCorrectPos('w','r','g')
        F()
    else:
        b = True
    if((cube[5][3] != cube[4][4]) or (cube[6][3] != cube[7][4]) or (cube[5][2] != cube[4][1])): # white/green/orange corner not in place
        F2()
        cornerToCorrectPos('w','g','o')
        F2()
    else:
        c = True
    if((cube[3][3] != cube[4][4]) or (cube[3][2] != cube[4][1]) or (cube[2][3] != cube[1][4])): # white/orange/blue not in place
        F()
        cornerToCorrectPos('w','o','b')
        Fi()
    else:
        d = True

    if a and b and c and d: return True
    else: return False

def midEdgeToCorrectPos(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)
    
    if edgeNum == 5:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 6:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 7:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 8:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 9:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 10:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 11:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')
    elif edgeNum == 12:
        print(edgeNum)
        if cube[edgePos[0][0]][edgePos[0][1]] == 'b': # c1
            print('b')
        elif cube[edgePos[0][0]][edgePos[0][1]] == 'r': # c2
            print('r')

def middleLayer():
    a, b, c, d = False, False, False, False
    if((cube[1][5] != cube[1][4]) or (cube[3][7] != cube[4][7])): # blue/red edge not in place
        print("BR")
        midEdgeToCorrectPos('b','r')
    else:
        a = True
    if((cube[5][7] != cube[4][7]) or (cube[7][5] != cube[7][4])): # red/green edge not in place
        print("RG")
    else:
        b = True
    if((cube[7][4] != cube[7][3]) or (cube[5][1] != cube[4][1])): # green/orange edge not in place
        print("GO")
    else:
        c = True
    if((cube[3][1] != cube[4][1]) or (cube[1][3] != cube[1][5])): # orange/blue edge not in place
        print("OB")
    else:
        d = True

    if a and b and c and d: return True
    else: return False

#------------------------------------------------------------------------------------------------------------------
# the following are helper functions, used to get some values, not used in program

# edges

# helper, used to create the edgeLinks array
cube2 = [['_', '_', '_', 'b',  3, 'b', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_',   1, 'b', 2, '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'b',   9, 'b', '_', '_', '_', '_', '_', '_'],
        ['o',   1, 'o', 'w',   9, 'w', 'r', 2, 'r', 'y', 3, 'y'],
        [ 8, 'o',    7,   7, 'w', 10, 10, 'r', 12, 12, 'y', 8],
        ['o',   6, 'o', 'w',  11, 'w', 'r', 5, 'r', 'y', 4, 'y'],
        ['_', '_', '_', 'g',  11, 'g', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_',   6, 'g', 5, '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'g',   4, 'g', '_', '_', '_', '_', '_', '_']]

def getEdges():
    e = []
    for i in range(1,13):
        for x in range(len(cube2)):
            for y in range(len(cube2[0])):
                if cube2[x][y] == i:
                    e.append([x,y])
    print(e)

def getEdgeColors():
    for x in edgeLinks:
        print(cube[x[0][0]][x[0][1]], cube[x[1][0]][x[1][1]])

def findEdge(x,y):
    e = [x,y]
    for i in range(len(edgeLinks)):
        if e in edgeLinks[i]:
            edgeIndex = edgeLinks[i]

    return edgeIndex
# end edges

# end helper functions