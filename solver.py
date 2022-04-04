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
    scramble = []
    for i in range(20):
        r = random.randint(0,len(moves) - 1)
        moves[r]()
        scramble.append(moves[r].__name__)
    solutionMoves.clear()
    return scramble

def printCube():
    for x in cube:
        print(x)

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

# solves the white cross, returns true if it did not perform any moves, false otherwise
def cross():
    a, b, c, d = False, False, False, False
    if((cube[3][4] != cube[4][4]) or (cube[2][4] != cube[1][4])): # top white/blue edge not in place AKA edge #1
        edgeToCorrectPos('w','b')
    else:
        a = True
    # edgeToCorrectPos was written for the white/blue edge, so if we rotate any white/<COLOR> edge to white/blue's place,
    # then we can perform the same algorithm but just take care of the rotation, 
    # hence the moves before and after the function call in the following if statements.
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

# returns the corner's coordinates based on the corner's colors, a, b, and c
def getCornerPos(a,b,c):
    for x in cornerLinks:
        if (a == cube[x[0][0]][x[0][1]] and b == cube[x[1][0]][x[1][1]] and c == cube[x[2][0]][x[2][1]]) or (a == cube[x[0][0]][x[0][1]] and c == cube[x[1][0]][x[1][1]] and b == cube[x[2][0]][x[2][1]]) or (b == cube[x[0][0]][x[0][1]] and a == cube[x[1][0]][x[1][1]] and c == cube[x[2][0]][x[2][1]]) or (c == cube[x[0][0]][x[0][1]] and a == cube[x[1][0]][x[1][1]] and b == cube[x[2][0]][x[2][1]]) or (c == cube[x[0][0]][x[0][1]] and b == cube[x[1][0]][x[1][1]] and a == cube[x[2][0]][x[2][1]]) or (b == cube[x[0][0]][x[0][1]] and c == cube[x[1][0]][x[1][1]] and a == cube[x[2][0]][x[2][1]]):
            return x

# getCornerNum returns the value of the edge
def getCornerNum(cPos):
    for i in range(len(cornerLinks)):
        if cPos == cornerLinks[i]:
            return i + 1

# performs specific moves based on the corner's position and orientation
def cornerToCorrectPos(c1,c2,c3):
    cornerPos = getCornerPos(c1,c2,c3)
    cornerNum = getCornerNum(cornerPos)

    if cornerNum == 1:
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            R()
            B()
            Ri()
            Bi()
            R()
            B()
            Ri()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c3:
            R()
            Bi()
            Ri()
            B()
            R()
            Bi()
            Ri()
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
        if cube[cornerPos[0][0]][cornerPos[0][1]] == c3:
            R()
            Li()
            Bi()
            L()
            Ri()
        elif cube[cornerPos[0][0]][cornerPos[0][1]] == c2:
            Li()
            B()
            L()
            B2()
            Ui()
            B()
            U()
            # U()
            # Bi()
            # Ui()
            # Bi()
            # R()
            # B2()
            # Ri()
            # Bi()
            # Bi()
            # Ui()
            # B()
            # U()
        else:
            Li()
            B2()
            L()
            Ui()
            B()
            U()
            # U()
            # Bi()
            # Ui()
            # Bi()
            # R()
            # B2()
            # Ri()
            # Bi()
            # Bi()
            # Ui()
            # B()
            # U()
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

# solves the white corners, returns true if it did not perform any moves, false otherwise
def corners():
    a, b, c, d = False, False, False, False

    if((cube[3][5] != cube[4][4]) or (cube[2][5] != cube[1][4]) or (cube[3][6] != cube[4][7])): # white/blue/red corner not in place
        cornerToCorrectPos('w','b','r')
    else:
        a = True
    # same as with edgeToCorrectPos, cornerToCorrectPos was written for the white/blue/red corner, so if we rotate any white/<COLOR>/<COLOR> corner to white/blue/red's place,
    # then we can perform the same algorithm but just take care of the rotation, 
    # hence the moves before and after the function call in the following if statements.
    if((cube[5][5] != cube[4][4]) or (cube[5][6] != cube[4][7]) or (cube[6][5] != cube[7][4])): # white/red/green corner not in place
        Fi() # move white/red/green corner to white/blue/red's place
        cornerToCorrectPos('w','r','g')
        F() # undo rotation
    else:
        b = True
    if((cube[5][3] != cube[4][4]) or (cube[6][3] != cube[7][4]) or (cube[5][2] != cube[4][1])): # white/green/orange corner not in place
        F2() # move white/green/orange corner to white/blue/red's place
        cornerToCorrectPos('w','g','o')
        F2() # undo rotation
    else:
        c = True
    if((cube[3][3] != cube[4][4]) or (cube[3][2] != cube[4][1]) or (cube[2][3] != cube[1][4])): # white/orange/blue not in place
        F() # move white/orange/blue corner to white/blue/orange's place
        cornerToCorrectPos('w','o','b')
        Fi() # undo rotation
    else:
        d = True

    if a and b and c and d: return True
    else: return False

# Algorithm to get an edge from the top layer into the left position in the middle layer
def leftEdgeAlg():
    Bi()
    Li()
    B()
    L()
    B()
    U()
    Bi()
    Ui()

# Algorithm to get an edge from the top layer into the right position in the middle layer
def rightEdgeAlg():
    B()
    R()
    Bi()
    Ri()
    Bi()
    Ui()
    B()
    U()

# Since we can't rotate the cube, then we need variations of the edge algorithms.
# leftEdgeAlg on right side
def leftEdgeAlgR():
    Bi()
    Ui()
    B()
    U()
    B()
    R()
    Bi()
    Ri()

# rightEdgeAlg on right side
def rightEdgeAlgR():
    B()
    D()
    Bi()
    Di()
    Bi()
    Ri()
    B()
    R()

# leftEdgeAlg on left side
def leftEdgeAlgL():
    Bi()
    Di()
    B()
    D()
    B()
    L()
    Bi()
    Li()

# rightEdgeAlg on left side
def rightEdgeAlgL():
    B()
    U()
    Bi()
    Ui()
    Bi()
    Li()
    B()
    L()

# leftEdgeAlg on bottom side
def leftEdgeAlgB():
    Bi()
    Ri()
    B()
    R()
    B()
    D()
    Bi()
    Di()

# rightEdgeAlg on bottm side
def rightEdgeAlgB():
    B()
    L()
    Bi()
    Li()
    Bi()
    Di()
    B()
    D()

# performs specific moves based on the middle blue/green edge's position and orientation
# unlike edgeToCorrectPos and cornerToCorrectPos, this function cannot be generalized
# because we are unable to rotate the middle edge if we consider the hardware limitations.
def midEdgeToCorrectPosBR(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)

    if edgeNum == 5:
        if cube[edgePos[0][0]][edgePos[0][1]] == c2:
            rightEdgeAlg()
            B2()
            rightEdgeAlg()
    elif edgeNum == 6:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            rightEdgeAlgR()
            B2()
            leftEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            rightEdgeAlgR()
            Bi()
            rightEdgeAlg()
    elif edgeNum == 7:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlgL()
            leftEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlgL()
            B()
            rightEdgeAlg()
    elif edgeNum == 8:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlg()
            B()
            leftEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlg()
            B2()
            rightEdgeAlg()
    elif edgeNum == 9:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            rightEdgeAlg()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Bi()
            leftEdgeAlgR()
    elif edgeNum == 10:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            rightEdgeAlg()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlgR()
    elif edgeNum == 11:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            leftEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B2()
            rightEdgeAlg()
    elif edgeNum == 12:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            Bi()
            rightEdgeAlg()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B2()
            leftEdgeAlgR()

# performs specific moves based on the middle green/red edge's position and orientation
def midEdgeToCorrectPosGR(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)

    if edgeNum == 6:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            rightEdgeAlgR()
            B2()
            rightEdgeAlgR()
    elif edgeNum == 7:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlgL()
            rightEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlgL()
            Bi()
            leftEdgeAlgB()
    elif edgeNum == 8:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlg()
            B()
            rightEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlg()
            leftEdgeAlgB()
    elif edgeNum == 9:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B2()
            leftEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Bi()
            rightEdgeAlgR()
    elif edgeNum == 10:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            Bi()
            leftEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            rightEdgeAlgR()
    elif edgeNum == 11:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            rightEdgeAlgR()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlgB()
    elif edgeNum == 12:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            leftEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B2()
            rightEdgeAlgR()

# performs specific moves based on the middle green/orange edge's position and orientation
def midEdgeToCorrectPosGO(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)

    if edgeNum == 7:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlgL()
            B2()
            leftEdgeAlgL()
    elif edgeNum == 8:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlg()
            Bi()
            leftEdgeAlgL()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlg()
            rightEdgeAlgB()
    elif edgeNum == 9:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B2()
            rightEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B()
            leftEdgeAlgL()
    elif edgeNum == 10:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            Bi()
            rightEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B2()
            leftEdgeAlgL()
    elif edgeNum == 11:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            Bi()
            leftEdgeAlgL()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            rightEdgeAlgB()
    elif edgeNum == 12:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            rightEdgeAlgB()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlgL()

# performs specific moves based on the middle orange/blue edge's position and orientation
def midEdgeToCorrectPosOB(c1,c2):
    edgePos = getEdgePos(c1,c2)
    edgeNum = getEdgeNum(edgePos)

    if edgeNum == 8:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            leftEdgeAlg()
            B2()
            leftEdgeAlg()
    elif edgeNum == 9:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B()
            rightEdgeAlgL()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            leftEdgeAlg()
    elif edgeNum == 10:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B2()
            rightEdgeAlgL()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            B()
            leftEdgeAlg()
    elif edgeNum == 11:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            B2()
            leftEdgeAlg()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Bi()
            rightEdgeAlgL()
    elif edgeNum == 12:
        if cube[edgePos[0][0]][edgePos[0][1]] == c1:
            rightEdgeAlgL()
        elif cube[edgePos[0][0]][edgePos[0][1]] == c2:
            Bi()
            leftEdgeAlg()

# solves the middle layer, returns true if it did not perform any moves, false otherwise
def middleLayer():
    a, b, c, d = False, False, False, False
    if((cube[1][5] != cube[1][4]) or (cube[3][7] != cube[4][7])): # blue/red edge not in place
        midEdgeToCorrectPosBR('b','r')
    else:
        a = True
    if((cube[5][7] != cube[4][7]) or (cube[7][5] != cube[7][4])): # red/green edge not in place
        midEdgeToCorrectPosGR('g','r') # cant think of a way to generalize this so had to create functions for the for middle edges
    else:
        b = True
    if((cube[7][4] != cube[7][3]) or (cube[5][1] != cube[4][1])): # green/orange edge not in place
        midEdgeToCorrectPosGO('g','o')
    else:
        c = True
    if((cube[3][1] != cube[4][1]) or (cube[1][3] != cube[1][5])): # orange/blue edge not in place
        midEdgeToCorrectPosOB('o','b')
    else:
        d = True

    if a and b and c and d: return True
    else: return False

# this function basically re-orients the cube so that the moves are performed as if the blue edge was the "main" face
# the input is a string of valid moves seperated by a space eg. "R D B U2i"
def movesInBlueOrientation(moves):
    m = moves.split()

    for move in m:
        if move == 'R':
            R()
        elif move == 'L':
            L()
        elif move == 'U':
            B()
        elif move == 'D':
            F()
        elif move == 'F':
            U()
        elif move == 'B':
            D()
        elif move == 'R2':
            R2()
        elif move == 'L2':
            L2()
        elif move == 'U2':
            B2()
        elif move == 'D2':
            F2()
        elif move == 'F2':
            U2()
        elif move == 'B2':
            D2()
        elif move == 'Ri':
            Ri()
        elif move == 'Li':
            Li()
        elif move == 'Ui':
            Bi()
        elif move == 'Di':
            Fi()
        elif move == 'Fi':
            Ui()
        elif move == 'Bi':
            Di()
        elif move == 'R2i':
            R2i()
        elif move == 'L2i':
            L2i()
        elif move == 'U2i':
            B2i()
        elif move == 'D2i':
            F2i()
        elif move == 'F2i':
            U2i()
        elif move == 'B2i':
            D2i()

# returns a string composed of x and y characters, where x is "any" color and y is the color yellow
def yellowOrientation():
    # the colors of the last layer a represented by the letters a-u
    # if we view the yellow face from above, with the blue face towards are the edges are:
    # a b c
    # d e f
    # g h i
    # if we hold the cube with the blue face towards us and yellow on top then j-u are the colors starting from
    # the top left blue corner, then going around the cube to the right, stopping at the top right orange corner
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u = cube[5][11], cube[5][10], cube[5][9], \
    cube[4][11], cube[4][10], cube[4][9], \
    cube[3][11], cube[3][10], cube[3][9], \
    cube[0][3], cube[0][4], cube[0][5], \
    cube[3][8], cube[4][8], cube[5][8], \
    cube[8][5], cube[8][4], cube[8][3], \
    cube[5][0], cube[4][0], cube[3][0]

    # the string created is in the order a-u as described above, this is used to recognize the orientation of the last layer
    orientation = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u
    orientation = list(orientation)

    for i in range(len(orientation)):
        if orientation[i] != 'y':
            orientation[i] = 'x'
    
    return ("".join(orientation))

# returns true if the last layer has been oriented, false otherwise
# each case is represented as a string which tells us the orientation of the yellow layer
# when an orientation is found, it performs the specific algorithm to orient the yellow face
def orientLastLayer():
    for i in range(4):
        orientation = yellowOrientation()
        #print(orientation)

        # Yellow completed
        if orientation == 'yyyyyyyyyxxxxxxxxxxxx':
            return(True)
        # All edges oriented
        elif orientation == 'xyyyyyxyxyxxyxxxxxyxx':
            movesInBlueOrientation("R U2 Ri Ui R Ui Ri")
            return(True)
        elif orientation == 'xyxyyyyyxxxyxxyxxyxxx':
            movesInBlueOrientation("R U Ri U R U2i Ri")
            return(True)
        elif orientation == 'xyxyyyxyxyxyxxxyxyxxx':
            movesInBlueOrientation("R U2 Ri Ui R U Ri Ui R Ui Ri")
            return(True)
        elif orientation == 'xyxyyyxyxxxyxxxyxxyxy':
            movesInBlueOrientation("R U2i R2i Ui R2 Ui R2i Ui Ui R")
            return(True)
        elif orientation == 'xyyyyyxyyyxxxxxxxyxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yyxyyyxyyyxxxxyxxxxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yyyyyyxyxyxyxxxxxxxxx':
            movesInBlueOrientation("R2 D Ri U2 R Di Ri U2 Ri")
            return(True)
        # T-shapes
        elif orientation == 'xxyyyyxxyyyxxxxxyyxxx':
            movesInBlueOrientation("R U Ri Ui Ri F R Fi")
            return(True)
        elif orientation == 'xxyyyyxxyxyxxxxxyxyxy':
            movesInBlueOrientation("F R U Ri Ui Fi")
            return(True)
        # Squares
        elif orientation == 'xxxxyyxyyxxxxxyxyyxyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xyyxyyxxxyyxyxxxxxyyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # C-shapes
        elif orientation == 'xxxyyyyxyxyxxxyxyxyxx':
            movesInBlueOrientation("R U R2i Ui Ri F R U R Ui Fi") 
            return(True)
        elif orientation == 'yyxxyxyyxxxxyyyxxxxyx':
            movesInBlueOrientation("Ri Ui Ri F R Fi U R")
            return(True)
        # W-shapes
        elif orientation == 'yxxyyxxyyyxxxyyxyxxxx':
            movesInBlueOrientation("") # ?
            return(False) # not yet implemented
        elif orientation == 'xyyyyxyxxxyxyyxxxyxxx':
            movesInBlueOrientation("R U Ri U R Ui Ri Ui Ri F R Fi")
            return(True)
        # Corners correct- flipped edges
        elif orientation == 'yyyyyxyxyxyxxyxxxxxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yxyyyyyxyxyxxxxxyxxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # P-shapes
        elif orientation == 'xyyxyyxxyyyxxxxxxyxyx':
            movesInBlueOrientation("Ri Ui F U R Ui Ri Fi R")
            return(True)
        elif orientation == 'xxyxyyxyyyxxxxxxyyxyx':
            movesInBlueOrientation("R U Bi Ui Ri U R B Ri")
            return(True)
        elif orientation == 'yxxyyxyyxxxxyyyxyxxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxyxyyxyyxxxxxxxyxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # I-shapes
        elif orientation == 'xxxyyyxxxxyyxxxyyxyxy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxyyyxxxxyxyxyxyxyxy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xyxxyxxyxyxxyyyxxyxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xyxxyxxyxxxxyyyxxxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # Fish shapes
        elif orientation == 'xyxyyxxxyyyxxyxyxxyxx':
            movesInBlueOrientation("R U Ri Ui Ri F R2 U Ri Ui Fi")
            return(True)
        elif orientation == 'xxyyyxxyxxxyxyxxyyxxy':
            movesInBlueOrientation("R U Ri U Ri F R Fi R U2i Ri")
            return(True)
        elif orientation == 'yxxxyyxyyyxxxxyxyxxyx':
            movesInBlueOrientation("R U2i R2i F R Fi R U2i Ri")
            return(True)
        elif orientation == 'yyxyyxxxyyyxxyyxxxxxx':
            movesInBlueOrientation("F R Ui Ri Ui R U Ri Fi")
            return(True)
        # Knight move shapes
        elif orientation == 'xxxyyyyxxxyyxxyxyyxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxyyyxxyyyxxxxyyxyxx':
            movesInBlueOrientation("Ri F R U Ri Fi R F Ui Fi")
            return(True)
        elif orientation == 'xxyyyyxxxyyxyxxxyxyxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxyyyxxyxyxxxyxyyxxy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # Awkward shapes
        elif orientation == 'yxyyyxxyxxxxyyxxyxxxy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yyxxyyyxxxyyxxxyxxxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xyxyyxyxyxyxxyxyxyxxx':
            movesInBlueOrientation("R U Ri U R U2i Ri F R U Ri Ui Fi")
            return(True)
        elif orientation == 'yxyyyxxyxyxyxyxxyxxxx':
            movesInBlueOrientation("Ri Ui R Ui Ri U2 R F R U Ri Ui Fi")
            return(True)
        # L-shapes
        elif orientation == 'xyxyyxxxxxyyxyxyxxyxy':
            movesInBlueOrientation("F R U Ri Ui R U Ri Ui Fi")
            return(True)
        elif orientation == 'xyxxyyxxxyyxyxyxxyxyx':
            movesInBlueOrientation("Fi Li Ui L U Li Ui L U F")
            return(True)
        elif orientation == 'xyxxyyxxxxyyxxxyxxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxxyyxyxxxyxxxyyxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxxyyxyxxxxyxyxyxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xyxxyyxxxxyxyxyxxxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        # Lightning bolts
        elif orientation == 'xyxyyxyxxxyyxyyxxyxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yxxyyxxyxyxxyyxyyxxxx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxxyyyyxxxyxxyxyyxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yyxxyyxxxyyxyxxyxxxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxyyyyyxxxyxyxxxyyxxx':
            movesInBlueOrientation("L Fi Li Ui L U F Ui Li")
            return(True)
        elif orientation == 'yxxyyyxxyxyxxxxyyxxxy':
            movesInBlueOrientation("Ri F R U Ri Ui Fi U R")
            return(True)
        # No edges flipped
        elif orientation == 'xxxxyxxxxxyxyyyxyxyyy':
            movesInBlueOrientation("R U2i R2i F R Fi U2i Ri F R Fi")
            return(True)
        elif orientation == 'xxxxyxxxxxyyxyxyyxyyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxxxyxxxyxyxxyyxyyxyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'xxyxyxxxxyyxyyxxyxyyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yxyxyxxxxyyyxyxxyxxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yxyxyxxxxxyxyyxxyxxyy':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        elif orientation == 'yxxxyxxxyxyxxyxyyxxyy':
            movesInBlueOrientation("R U Ri U Ri F R Fi U2i Ri F R Fi")
            return(True)
        elif orientation == 'yxyxyxyxyxyxxyxxyxxyx':
            movesInBlueOrientation("") # convert
            return(False) # not yet implemented
        else:
            movesInBlueOrientation("U")

    return(False)

# returns a list of 4 possible permutatioin of the last layer. The list contains four strings that are composed
# of the numbers 1, 2, 3, and 0. These numbers represent a color, if we hold the cube with the blue face
# towards us and yellow on top, the colors starting from the top left blue corner, then going around the cube to the right, stopping at the top right orange corner.
# There are four so that we can detect a permutation but also the same permutation if the colors were switched so all cases are considered.
def yellowPermutation():
    j,k,l,m,n,o,p,q,r,s,t,u = cube[0][3], cube[0][4], cube[0][5], \
    cube[3][8], cube[4][8], cube[5][8], \
    cube[8][5], cube[8][4], cube[8][3], \
    cube[5][0], cube[4][0], cube[3][0]

    orientation = j+k+l+m+n+o+p+q+r+s+t+u
    orientation = list(orientation)

    orientations = []

    for i in range(4):
        temp = deepcopy(orientation)

        for j in range(len(temp)):
            if temp[j] == 'b':
                temp[j] = str((1 + i) % 4)
            if temp[j] == 'r':
                temp[j] = str((2 + i) % 4)
            if temp[j] == 'g':
                temp[j] = str((3 + i) % 4)
            if temp[j] == 'o':
                temp[j] = str((4 + i) % 4)
        
        orientations.append("".join(temp))
    
    return orientations

# returns true if the permutation is found, false otherwise
# each case is represented as a string which tells us which permutation we have.
# once a permutation is found, an algorithm is executed, which solves the cube
def permuteLastLayer():
    for i in range(4):
        permutation = yellowPermutation()

        # Permute edges only
        if '111222333000' in permutation:
            return(True)
        elif '323030111202' in permutation:
            movesInBlueOrientation("R2 U R U Ri Ui Ri Ui Ri U Ri")
            return(True)
        elif '303020111232' in permutation:
            movesInBlueOrientation("R Ui R U R U R Ui Ri Ui R2")
            return(True)
        elif '303030121212' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        elif '202313020131' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        # Permute corners only
        elif '220132303011' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        elif '223030102311' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        elif '123032301210' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        # Swap one set of adjacent corners
        elif '330103021212' in permutation:
            movesInBlueOrientation("R Ui Ri Ui R U R D Ri Ui R Di Ri U2 Ri Ui")
            return(True)
        elif '232320103011' in permutation:
            movesInBlueOrientation("Ri U2 R U2i Ri F R U Ri Ui Ri Fi R2 Ui")
            return(True)
        elif '333001220112' in permutation:
            movesInBlueOrientation("Ri U Li U2 R Ui Ri U2 R L Ui")
            return(True)
        elif '233022300111' in permutation:
            movesInBlueOrientation("R U Ri Fi R U Ri Ui Ri F R2 Ui Ri Ui")
            return(True)
        elif '223012300131' in permutation:
            movesInBlueOrientation("R U Ri Ui Ri F R2 Ui Ri Ui R U Ri Fi")
            return(True)
        elif '310103031222' in permutation:
            movesInBlueOrientation("Ri Ui Fi R U Ri Ui Ri F R2 Ui Ri Ui R U Ri U R")
            return(True)
        # Swap one set of diagonal corners
        elif '220103032311' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        elif '220133012301' in permutation:
            movesInBlueOrientation("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi")
            return(True)
        elif '022311200133' in permutation:
            movesInBlueOrientation("R U Ri U R U Ri Fi R U Ri Ui Ri F R2 Ui Ri U2 R Ui Ri")
            return(True)
        elif '220113002331' in permutation:
            movesInBlueOrientation("Ri U R Ui Ri Fi Ui F R U Ri F Ri Fi R Ui R")
            return(True)
        # G permutations
        elif '122301213030' in permutation:
            movesInBlueOrientation("R2 U Ri U Ri Ui R Ui R2 D Ui Ri U R Di U")
            return(True)
        elif '311203020132' in permutation:
            movesInBlueOrientation("")
            return(False) # not yet implemented
        elif '132301223010' in permutation:
            movesInBlueOrientation("R2 Ui R Ui R U Ri U R2 Di U R Ui Ri D Ui")
            return(True)
        elif '102331213020' in permutation:
            movesInBlueOrientation("Di R U Ri Ui D R2 Ui R Ui Ri U Ri U R2 U")
            return(True)
        else:
            movesInBlueOrientation('U')
    print("Not found", permutation)
    return(False)

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