import Face


class cube:
    def __init__(self, uface: Face, lface: Face, fface: Face, rface: Face, bface: Face, dface: Face, moves: str) -> None:
        self.uface = uface
        self.lface = lface
        self.fface = fface
        self.rface = rface
        self.bface = bface
        self.dface = dface
        self.moves = moves

    # probably a better way to do this but I was tired
    def show_cube(self):
        '''Allows to visualize the current state of the cube'''
        for i in range(3):
            print("  "*3+" ", self.uface.state[i][0],
                  self.uface.state[i][1], self.uface.state[i][2])
        print("")
        for i in range(3):
            print(self.lface.state[i][0], self.lface.state[i][1], self.lface.state[i][2], " ", self.fface.state[i][0], self.fface.state[i][1], self.fface.state[i][2],
                  " ", self.rface.state[i][0], self.rface.state[i][1], self.rface.state[i][2], " ", self.bface.state[i][0], self.bface.state[i][1], self.bface.state[i][2])
        print("")
        for i in range(3):
            print("  "*3+" ", self.dface.state[i][0],
                  self.dface.state[i][1], self.dface.state[i][2])

    # all of the moving moves are void
    # technically there are also exist slice moves (M, E, S) and wide moves (i.e. moving two right layers at once) however since they are very uncommon and not used in the beginner layer by layer method they have been ommitted
    def R(self) -> None:
        '''Performs an R move on the cube. An R move is one clockwise move of the righthandside face '''
        self.rface.rotate_clockwise()
        temp1, temp2, temp3 = self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][2]
        self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][
            2] = self.dface.state[0][2], self.dface.state[1][2], self.dface.state[2][2]
        self.dface.state[0][2], self.dface.state[1][2], self.dface.state[2][
            2] = self.bface.state[2][0], self.bface.state[1][0], self.bface.state[0][0]
        self.bface.state[0][0], self.bface.state[1][0], self.bface.state[2][
            0] = self.uface.state[2][2], self.uface.state[1][2], self.uface.state[0][2]
        self.uface.state[0][2], self.uface.state[1][2], self.uface.state[2][2] = temp1, temp2, temp3
        self.moves += "R "

    # p stands for prime, ie counterclockwise rotation
    def Rp(self):
        '''Performs an R' move on the cube. An R' move is one counterclockwise move of the righthandside face'''
        self.rface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][2]
        self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][
            2] = self.uface.state[0][2], self.uface.state[1][2], self.uface.state[2][2]
        self.uface.state[0][2], self.uface.state[1][2], self.uface.state[2][
            2] = self.bface.state[2][0], self.bface.state[1][0], self.bface.state[0][0]
        self.bface.state[2][0], self.bface.state[1][0], self.bface.state[0][
            0] = self.dface.state[0][2], self.dface.state[1][2], self.dface.state[2][2]
        self.dface.state[0][2], self.dface.state[1][2], self.dface.state[2][2] = temp1, temp2, temp3
        self.moves += "R' "

    # as before, this could be done by calling R() twice but this should be faster
    def R2(self):
        '''Performs an R2 move on the cube. An R2 move is a double turn of the righthandside face'''
        self.rface.rotate_180()
        temp1, temp2, temp3 = self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][2]
        self.fface.state[0][2], self.fface.state[1][2], self.fface.state[2][2], self.bface.state[0][0], self.bface.state[1][
            0], self.bface.state[2][0] = self.bface.state[2][0], self.bface.state[1][0], self.bface.state[0][0], temp3, temp2, temp1
        temp1, temp2, temp3 = self.uface.state[0][2], self.uface.state[1][2], self.uface.state[2][2]
        self.uface.state[0][2], self.uface.state[1][2], self.uface.state[2][2], self.dface.state[0][2], self.dface.state[1][
            2], self.dface.state[2][2] = self.dface.state[0][2], self.dface.state[1][2], self.dface.state[2][2], temp1, temp2, temp3
        self.moves += "R2 "
    
    #all of the further moves are defined just as the R moves
    #just a letter - one clockwise turn of corresponding face
    #letter with a ' - one counterclockwise turn of corresponsing face
    #letter followed by a 2 -double turn of said face

    def L(self):
        '''Performs an L move on the cube.'''
        self.lface.rotate_clockwise()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][0]
        self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][
            0] = self.uface.state[0][0], self.uface.state[1][0], self.uface.state[2][0]
        self.uface.state[0][0], self.uface.state[1][0], self.uface.state[2][
            0] = self.bface.state[2][2], self.bface.state[1][2], self.bface.state[0][2]
        self.bface.state[0][2], self.bface.state[1][2], self.bface.state[2][
            2] = self.dface.state[2][0], self.dface.state[1][0], self.dface.state[0][0]
        self.dface.state[0][0], self.dface.state[1][0], self.dface.state[2][0] = temp1, temp2, temp3
        self.moves += "L "

    def Lp(self):
        '''Performs an L' move on the cube.'''
        self.lface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][0]
        self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][
            0] = self.dface.state[0][0], self.dface.state[1][0], self.dface.state[2][0]
        self.dface.state[0][0], self.dface.state[1][0], self.dface.state[2][
            0] = self.bface.state[2][2], self.bface.state[1][2], self.bface.state[0][2]
        self.bface.state[0][2], self.bface.state[1][2], self.bface.state[2][
            2] = self.uface.state[2][0], self.uface.state[1][0], self.uface.state[0][0]
        self.uface.state[0][0], self.uface.state[1][0], self.uface.state[2][0] = temp1, temp2, temp3
        self.moves += "L' "

    def L2(self):
        '''Performs an L2 move on the cube'''
        self.lface.rotate_180()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][0]
        self.fface.state[0][0], self.fface.state[1][0], self.fface.state[2][0], self.bface.state[0][2], self.bface.state[1][
            2], self.bface.state[2][2] = self.bface.state[2][2], self.bface.state[1][2], self.bface.state[0][2], temp3, temp2, temp1
        temp1, temp2, temp3 = self.uface.state[0][0], self.uface.state[1][0], self.uface.state[2][0]
        self.uface.state[0][0], self.uface.state[1][0], self.uface.state[2][0], self.dface.state[0][0], self.dface.state[1][
            0], self.dface.state[2][0] = self.dface.state[0][0], self.dface.state[1][0], self.dface.state[2][0], temp1, temp2, temp3
        self.moves += "L2 "

    def U(self):
        '''Performs a U move on the cube'''
        self.uface.rotate_clockwise()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][2]
        self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][
            2] = self.rface.state[0][0], self.rface.state[0][1], self.rface.state[0][2]
        self.rface.state[0][0], self.rface.state[0][1], self.rface.state[0][
            2] = self.bface.state[0][0], self.bface.state[0][1], self.bface.state[0][2]
        self.bface.state[0][0], self.bface.state[0][1], self.bface.state[0][
            2] = self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][2]
        self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][2] = temp1, temp2, temp3
        self.moves += "U "

    def Up(self):
        '''Performs a U' move on the cube.'''
        self.uface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][2]
        self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][
            2] = self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][2]
        self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][
            2] = self.bface.state[0][0], self.bface.state[0][1], self.bface.state[0][2]
        self.bface.state[0][0], self.bface.state[0][1], self.bface.state[0][
            2] = self.rface.state[0][0], self.rface.state[0][1], self.rface.state[0][2]
        self.rface.state[0][0], self.rface.state[0][1], self.rface.state[0][2] = temp1, temp2, temp3
        self.moves += "U' "

    def U2(self):
        '''Performs a U2 move on the cube'''
        self.uface.rotate_180()
        temp1, temp2, temp3 = self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][2]
        self.fface.state[0][0], self.fface.state[0][1], self.fface.state[0][2], self.bface.state[0][0], self.bface.state[0][
            1], self.bface.state[0][2] = self.bface.state[0][0], self.bface.state[0][1], self.bface.state[0][2], temp1, temp2, temp3
        temp1, temp2, temp3 = self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][2]
        self.lface.state[0][0], self.lface.state[0][1], self.lface.state[0][2], self.rface.state[0][0], self.rface.state[0][
            1], self.rface.state[0][2] = self.rface.state[0][0], self.rface.state[0][1], self.rface.state[0][2], temp1, temp2, temp3
        self.moves += "U2 "

    def D(self):
        '''Performs a D move on the cube'''
        self.dface.rotate_clockwise()
        temp1, temp2, temp3 = self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][2]
        self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][
            2] = self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][2]
        self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][
            2] = self.bface.state[2][0], self.bface.state[2][1], self.bface.state[2][2]
        self.bface.state[2][0], self.bface.state[2][1], self.bface.state[2][
            2] = self.rface.state[2][0], self.rface.state[2][1], self.rface.state[2][2]
        self.rface.state[2][0], self.rface.state[2][1], self.rface.state[2][2] = temp1, temp2, temp3
        self.moves += "D "

    def Dp(self):
        '''Performs a D' move on the cube'''
        self.dface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][2]
        self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][
            2] = self.rface.state[2][0], self.rface.state[2][1], self.rface.state[2][2]
        self.rface.state[2][0], self.rface.state[2][1], self.rface.state[2][
            2] = self.bface.state[2][0], self.bface.state[2][1], self.bface.state[2][2]
        self.bface.state[2][0], self.bface.state[2][1], self.bface.state[2][
            2] = self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][2]
        self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][2] = temp1, temp2, temp3
        self.moves += "D' "

    def D2(self):
        '''Performs a D2 move on the cube'''
        self.uface.rotate_180()
        temp1, temp2, temp3 = self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][2]
        self.fface.state[2][0], self.fface.state[2][1], self.fface.state[2][2], self.bface.state[2][0], self.bface.state[2][
            1], self.bface.state[2][2] = self.bface.state[2][0], self.bface.state[2][1], self.bface.state[2][2], temp1, temp2, temp3
        temp1, temp2, temp3 = self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][2]
        self.lface.state[2][0], self.lface.state[2][1], self.lface.state[2][2], self.rface.state[2][0], self.rface.state[2][
            1], self.rface.state[2][2] = self.rface.state[2][0], self.rface.state[2][1], self.rface.state[2][2], temp1, temp2, temp3
        self.moves += "D2 "

    def F(self):
        '''Performs an F move on the cube'''
        self.fface.rotate_clockwise()
        temp1, temp2, temp3 = self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][2]
        self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][
            2] = self.lface.state[2][2], self.lface.state[1][2], self.lface.state[0][2]
        self.lface.state[0][2], self.lface.state[1][2], self.lface.state[2][
            2] = self.dface.state[0][0], self.dface.state[0][1], self.dface.state[0][2]
        self.dface.state[0][0], self.dface.state[0][1], self.dface.state[0][
            2] = self.rface.state[2][0], self.rface.state[1][0], self.rface.state[0][0]
        self.rface.state[0][0], self.rface.state[1][0], self.rface.state[2][0] = temp1, temp2, temp3
        self.moves += "F "

    def Fp(self):
        '''Performs an F' move on the cube'''
        self.fface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][2]
        self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][
            2] = self.rface.state[0][0], self.rface.state[1][0], self.rface.state[2][0]
        self.rface.state[0][0], self.rface.state[1][0], self.rface.state[2][
            0] = self.dface.state[0][2], self.dface.state[0][1], self.dface.state[0][0]
        self.dface.state[0][0], self.dface.state[0][1], self.dface.state[0][
            2] = self.lface.state[0][2], self.lface.state[1][2], self.lface.state[2][2]
        self.lface.state[0][2], self.lface.state[1][2], self.lface.state[2][2] = temp3, temp2, temp1
        self.moves += "F' "

    def F2(self):
        '''Performs an F2 move on the cube'''
        self.fface.rotate_180()
        temp1, temp2, temp3 = self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][2]
        self.uface.state[2][0], self.uface.state[2][1], self.uface.state[2][2], self.dface.state[0][0], self.dface.state[0][
            1], self.dface.state[0][2] = self.dface.state[0][2], self.dface.state[0][1], self.dface.state[0][0], temp3, temp2, temp1
        temp1, temp2, temp3 = self.rface.state[0][0], self.rface.state[1][0], self.rface.state[2][0]
        self.rface.state[0][0], self.rface.state[1][0], self.rface.state[2][0], self.lface.state[0][2], self.lface.state[1][
            2], self.lface.state[2][2] = self.lface.state[2][2], self.lface.state[1][2], self.lface.state[0][2], temp3, temp2, temp1
        self.moves += "F2 "

    def B(self):
        '''Performs a B move on the cube'''
        self.bface.rotate_clockwise()
        temp1, temp2, temp3 = self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][2]
        self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][
            2] = self.rface.state[0][2], self.rface.state[1][2], self.rface.state[2][2]
        self.rface.state[0][2], self.rface.state[1][2], self.rface.state[2][
            2] = self.dface.state[2][2], self.dface.state[2][1], self.dface.state[2][0]
        self.dface.state[2][0], self.dface.state[2][1], self.dface.state[2][
            2] = self.lface.state[0][0], self.lface.state[1][0], self.lface.state[2][0]
        self.lface.state[0][0], self.lface.state[1][0], self.lface.state[2][0] = temp3, temp2, temp1
        self.moves += "B "

    def Bp(self):
        '''Performs a B' move on the cube'''
        self.bface.rotate_counterclockwise()
        temp1, temp2, temp3 = self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][2]
        self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][
            2] = self.lface.state[2][0], self.lface.state[1][0], self.lface.state[0][0]
        self.lface.state[0][0], self.lface.state[1][0], self.lface.state[2][
            0] = self.dface.state[2][0], self.dface.state[2][1], self.dface.state[2][2]
        self.dface.state[2][0], self.dface.state[2][1], self.dface.state[2][
            2] = self.rface.state[2][2], self.rface.state[1][2], self.rface.state[0][2]
        self.rface.state[0][2], self.rface.state[1][2], self.rface.state[2][2] = temp1, temp2, temp3
        self.moves += "B' "

    def B2(self):
        '''Performs a B2 move on the cube'''
        self.bface.rotate_180()
        temp1, temp2, temp3 = self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][2]
        self.uface.state[0][0], self.uface.state[0][1], self.uface.state[0][2], self.dface.state[2][0], self.dface.state[2][
            1], self.dface.state[2][2] = self.dface.state[2][2], self.dface.state[2][1], self.dface.state[2][0], temp3, temp2, temp1
        temp1, temp2, temp3 = self.rface.state[0][2], self.rface.state[1][2], self.rface.state[2][2]
        self.rface.state[0][2], self.rface.state[1][2], self.rface.state[2][2], self.lface.state[0][0], self.lface.state[1][
            0], self.lface.state[2][0] = self.lface.state[2][0], self.lface.state[1][0], self.lface.state[0][0], temp3, temp2, temp1
        self.moves += "B2 "

    '''The following are whole cube rotations'''
    def x(self):
        '''Performs an x rotation on the cube, i.e. the down face is now the front face'''
        temp = self.uface
        self.uface = self.fface
        self.fface = self.dface
        self.bface.rotate_180()
        self.dface = self.bface
        temp.rotate_180()
        self.bface = temp
        self.lface.rotate_counterclockwise()
        self.rface.rotate_clockwise()
        self.moves += "x "

    def xp(self):
        '''Performs an x' rotation on the cube'''
        temp = self.dface
        self.dface = self.fface
        self.fface = self.uface
        self.bface.rotate_180()
        self.uface = self.bface
        temp.rotate_180()
        self.bface = temp
        self.rface.rotate_counterclockwise()
        self.lface.rotate_clockwise()
        self.moves += "x' "

    def x2(self):
        '''Performs an x2 rotation on the cube'''
        temp = self.dface
        self.dface, self.uface = self.uface, temp
        self.bface.rotate_180()
        self.fface.rotate_180()
        temp = self.bface
        self.bface, self.fface = self.fface, temp
        self.rface.rotate_180()
        self.lface.rotate_180()
        self.moves += "x2 "

    def y(self):
        '''Performs a y rotation on the cube, where the previous right face now becomes the front face'''
        temp = self.fface
        self.fface, self.rface, self.bface, self.lface = self.rface, self.bface, self.lface, temp
        self.uface.rotate_clockwise()
        self.dface.rotate_counterclockwise()
        self.moves += "y "

    def yp(self):
        '''Performs a y' rotation on the cube'''
        temp = self.fface
        self.fface, self.lface, self.bface, self.rface = self.lface, self.bface, self.rface, temp
        self.dface.rotate_clockwise()
        self.uface.rotate_counterclockwise()
        self.moves += "y' "

    def y2(self):
        '''performs a y2 rotation on the cube'''
        temp = self.fface
        self.fface, self.bface = self.bface, temp
        temp = self.lface
        self.lface, self.rface = self.rface, temp
        self.dface.rotate_180()
        self.uface.rotate_180()
        self.moves += "y2 "

    # probably won't be used much but in case it is I'll add it
    def z(self):
        '''performs a z rotation on the cube, where the previous up face now becomes the right face'''
        temp = self.uface
        self.lface.rotate_clockwise()
        self.uface = self.lface
        self.dface.rotate_clockwise()
        self.lface = self.dface
        self.rface.rotate_clockwise()
        self.dface = self.rface
        temp.rotate_clockwise()
        self.rface = temp
        self.fface.rotate_clockwise()
        self.bface.rotate_counterclockwise()
        self.moves += "z "

    def zp(self):
        '''performs a z' rotation on the cube'''
        temp = self.uface
        self.rface.rotate_counterclockwise()
        self.uface = self.rface
        self.dface.rotate_counterclockwise()
        self.rface = self.dface
        self.lface.rotate_counterclockwise()
        self.dface = self.lface
        temp.rotate_counterclockwise()
        self.lface = temp
        self.bface.rotate_clockwise()
        self.fface.rotate_counterclockwise()
        self.moves += "z' "

    def z2(self):
        '''performs a z2 rotation on the cube'''
        temp = self.uface
        self.dface.rotate_180()
        self.uface = self.dface
        temp.rotate_180()
        self.dface = temp
        temp = self.lface
        self.rface.rotate_180()
        self.lface = self.rface
        temp.rotate_180()
        self.rface = temp
        self.bface.rotate_180()
        self.fface.rotate_180()
        self.moves += "z2 "
