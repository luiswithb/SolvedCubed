from copy import deepcopy

cube = [['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'b', 'b', 'b', '_', '_', '_', '_', '_', '_'],
        ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
        ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
        ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
        ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', 'g', 'g', 'g', '_', '_', '_', '_', '_', '_']]

solutionMoves = []

# Before change
#   012 345 678 910111
# 0     bbb
# 1     bbb
# 2     bbb
# 3 ooo www rrr yyy
# 4 ooo www rrr yyy
# 5 ooo www rrr yyy
# 6     ggg
# 7     ggg
# 8     ggg
 
# After change
#   012 345 678 901
# 0     wwr
# 1     wwr
# 2     wwr
# 3 ggg rry bbb woo
# 4 ggg rry bbb woo
# 5 ggg rry bbb woo
# 6     yyo
# 7     yyo
# 8     yyo
 
def R():
    previous_state = deepcopy(cube)
 
    #move g to w
    cube[3][5] = previous_state[6][5]
    cube[4][5] = previous_state[7][5]
    cube[5][5] = previous_state[8][5]
 
    #move w to b
    cube[0][5] = previous_state[3][5]
    cube[1][5] = previous_state[4][5]
    cube[2][5] = previous_state[5][5]
 
    #move b to y
    cube[5][9] = previous_state[0][5]
    cube[4][9] = previous_state[1][5]
    cube[3][9] = previous_state[2][5]
 
    #move y to g
    cube[6][5] = previous_state[5][9]
    cube[7][5] = previous_state[4][9]
    cube[8][5] = previous_state[3][9]
    
    #move current face
    cube[4][8] = previous_state[3][7]
    cube[5][8] = previous_state[3][8]
    cube[5][7] = previous_state[4][8]
    cube[5][6] = previous_state[5][8]
    cube[4][6] = previous_state[5][7]
    cube[3][6] = previous_state[5][6]
    cube[3][7] = previous_state[4][6]
    cube[3][8] = previous_state[3][6]
    solutionMoves.append(R)
def L():
    previous_state = deepcopy(cube)
    
    #move b to w
    cube[3][3] = previous_state[0][3]
    cube[4][3] = previous_state[1][3]
    cube[5][3] = previous_state[2][3]
    
    #move y to b
    cube[0][3] = previous_state[5][11]
    cube[1][3] = previous_state[4][11]
    cube[2][3] = previous_state[3][11]
    
    #move g to y
    cube[5][11] = previous_state[6][3]
    cube[4][11] = previous_state[7][3]
    cube[3][11] = previous_state[8][3]
    
    #move w to g
    cube[6][3] = previous_state[3][3]
    cube[7][3] = previous_state[4][3]
    cube[8][3] = previous_state[5][3]
    
    #move current face
    cube[4][2] = previous_state[3][1]
    cube[5][2] = previous_state[3][2]
    cube[5][1] = previous_state[4][2]
    cube[5][0] = previous_state[5][2]
    cube[4][0] = previous_state[5][1]
    cube[3][0] = previous_state[5][0]
    cube[3][1] = previous_state[4][0]
    cube[3][2] = previous_state[3][0]
    solutionMoves.append(L)
def U():
    previous_state = deepcopy(cube)
    
    #move r to w
    cube[3][3] = previous_state[3][6]
    cube[3][4] = previous_state[3][7]
    cube[3][5] = previous_state[3][8]
    
    #move w to o
    cube[3][0] = previous_state[3][3]
    cube[3][1] = previous_state[3][4]
    cube[3][2] = previous_state[3][5]
    
    #move o to y
    cube[3][9] = previous_state[3][0]
    cube[3][10] = previous_state[3][1]
    cube[3][11] = previous_state[3][2]
    
    #move y to r
    cube[3][6] = previous_state[3][9]
    cube[3][7] = previous_state[3][10]
    cube[3][8] = previous_state[3][11]
    
    #move current face
    cube[1][5] = previous_state[0][4]
    cube[2][5] = previous_state[0][5]
    cube[2][4] = previous_state[1][5]
    cube[2][3] = previous_state[2][5]
    cube[1][3] = previous_state[2][4]
    cube[0][3] = previous_state[2][3]
    cube[0][4] = previous_state[1][3]
    cube[0][5] = previous_state[0][3]
    solutionMoves.append(U)
def D():
    previous_state = deepcopy(cube)
    
    #move o to w
    cube[5][3] = previous_state[5][0]
    cube[5][4] = previous_state[5][1]
    cube[5][5] = previous_state[5][2]
    
    #move w to r
    cube[5][6] = previous_state[5][3]
    cube[5][7] = previous_state[5][4]
    cube[5][8] = previous_state[5][5]
    
    #move r to y
    cube[5][9] = previous_state[5][6]
    cube[5][10] = previous_state[5][7]
    cube[5][11] = previous_state[5][8]
    
    #move y to o
    cube[5][0] = previous_state[5][9]
    cube[5][1] = previous_state[5][10]
    cube[5][2] = previous_state[5][11]
    
    #move current face
    cube[7][5] = previous_state[6][4]
    cube[8][5] = previous_state[6][5]
    cube[8][4] = previous_state[7][5]
    cube[8][3] = previous_state[8][5]
    cube[7][3] = previous_state[8][4]
    cube[6][3] = previous_state[8][3]
    cube[6][4] = previous_state[7][3]
    cube[6][5] = previous_state[6][3]
    solutionMoves.append(D)
def F():
    previous_state = deepcopy(cube)
    
    #move o to b
    cube[2][3] = previous_state[5][2]
    cube[2][4] = previous_state[4][2]
    cube[2][5] = previous_state[3][2]
    
    #move b to r
    cube[3][6] = previous_state[2][3]
    cube[4][6] = previous_state[2][4]
    cube[5][6] = previous_state[2][5]
    
    #move r to g
    cube[6][5] = previous_state[3][6]
    cube[6][4] = previous_state[4][6]
    cube[6][3] = previous_state[5][6]
    
    #move g to o
    cube[5][2] = previous_state[6][5]
    cube[4][2] = previous_state[6][4]
    cube[3][2] = previous_state[6][3]
    
    #move current face
    cube[4][5] = previous_state[3][4]
    cube[5][5] = previous_state[3][5]
    cube[5][4] = previous_state[4][5]
    cube[5][3] = previous_state[5][5]
    cube[4][3] = previous_state[5][4]
    cube[3][3] = previous_state[5][3]
    cube[3][4] = previous_state[4][3]
    cube[3][5] = previous_state[3][3]
    solutionMoves.append(F)
def B():
    previous_state = deepcopy(cube)
    
    #move r to b
    cube[0][3] = previous_state[3][8]
    cube[0][4] = previous_state[4][8]
    cube[0][5] = previous_state[5][8]
    
    #move b to o
    cube[5][0] = previous_state[0][3]
    cube[4][0] = previous_state[0][4]
    cube[3][0] = previous_state[0][5]
    
    #move o to g
    cube[8][5] = previous_state[5][0]
    cube[8][4] = previous_state[4][0]
    cube[8][3] = previous_state[3][0]
    
    #move g to r
    cube[3][8] = previous_state[8][5]
    cube[4][8] = previous_state[8][4]
    cube[5][8] = previous_state[8][3]
    
    #move current face
    cube[4][11] = previous_state[3][10]
    cube[5][11] = previous_state[3][11]
    cube[5][10] = previous_state[4][11]
    cube[5][9] = previous_state[5][11]
    cube[4][9] = previous_state[5][10]
    cube[3][9] = previous_state[5][9]
    cube[3][10] = previous_state[4][9]
    cube[3][11] = previous_state[3][9]
    solutionMoves.append(B)

def R2():
    for i in range(2):
        R()
def L2():
    for i in range(2):
        L()
def U2():
    for i in range(2):
        U()
def D2():
    for i in range(2):
        D()
def F2():
    for i in range(2):
        F()
def B2():
    for i in range(2):
        B()
def Ri():
    for i in range(3):
        R()
def Li():
    for i in range(3):
        L()
def Ui():
    for i in range(3):
        U()
def Di():
    for i in range(3):
        D()
def Fi():
    for i in range(3):
        F()
def Bi():
    for i in range(3):
        B()
def R2i():
    for i in range(2):
        Ri()
def L2i():
    for i in range(2):
        Li()
def U2i():
    for i in range(2):
        Ui()
def D2i():
    for i in range(2):
        Di()
def F2i():
    for i in range(2):
        Fi()
def B2i():
    for i in range(2):
        Bi()