class solver:
    '''This class will contain a Solver for the cube.'''
    # To DO:
    # implement daisy maker
    # improve f2l
    # improve cross aligner
    # improve is top right correct method

    def __init__(self, cube) -> None:
        self.cube = cube

    # some useful algorithms
    def sexy_move(self):
        ''' Multipurpose sequence, commonly known as sexy move'''
        self.cube.R()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()

    def reverse_sexy_move(self):
        '''Other multipurpose sequence'''
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()

    def move_corners_clockwise(self):
        '''Used to move corners of the last layer around'''
        self.cube.Lp()
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.L()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()

    def move_cross_pieces(self):
        '''Used to move around edge pieces of the last layer'''
        self.cube.Up()
        self.cube.R()
        self.cube.U2()
        self.cube.Rp()
        self.cube.Up()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()

    def make_a_cross(self):
        '''Used to make a cross on the last layer'''
        self.cube.F()
        self.sexy_move()
        self.cube.Fp()

    def insert_f2l_left(self):
        '''Used to insert an edge belonging in the middle layer on the left'''
        self.cube.Up()
        self.cube.Lp()
        self.cube.U()
        self.cube.L()
        self.cube.yp()
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
        self.cube.y()

    def insert_f2l_right(self):
        '''Used to insert an edge belonging in the middle layer on the right'''
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
        self.cube.y()
        self.cube.Up()
        self.cube.Lp()
        self.cube.U()
        self.cube.L()
        self.cube.yp()

    # some checking methods
    def is_top_right_corner_correct(self) -> bool:
        '''Check if the corner positioned in the top right
        of the front face is in the correct position'''
        if self.cube.uface.state[2][2] == self.cube.uface.state[1][1] and self.cube.fface.state[0][2] == self.cube.fface.state[1][1] and self.cube.rface.state[0][0] == self.cube.rface.state[1][1]:
            return True
        elif self.cube.uface.state[2][2] == self.cube.rface.state[1][1] and self.cube.fface.state[0][2] == self.cube.uface.state[1][1] and self.cube.rface.state[0][0] == self.cube.fface.state[1][1]:
            return True
        elif self.cube.uface.state[2][2] == self.cube.fface.state[1][1] and self.cube.fface.state[0][2] == self.cube.rface.state[1][1] and self.cube.rface.state[0][0] == self.cube.uface.state[1][1]:
            return True
        else:
            return False

    def is_edge_in_top_layer(self, colors) -> bool:
        '''Method used for looking for a piece in the top layer'''
        if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
            return True
        if self.cube.lface.state[0][1] in colors and self.cube.uface.state[1][0] in colors:
            return True
        if self.cube.rface.state[0][1] in colors and self.cube.uface.state[1][2] in colors:
            return True
        if self.cube.bface.state[0][1] in colors and self.cube.uface.state[0][1] in colors:
            return True
        return False

    def is_corner_in_bottom_layer(self, colors):
        '''Method used for checking whether a given corner is located in the bottom layer'''
        if self.cube.fface.state[2][2] in colors and self.cube.rface.state[2][0] in colors and self.cube.dface.state[0][2] in colors:
            return True
        if self.cube.rface.state[2][2] in colors and self.cube.bface.state[2][0] in colors and self.cube.dface.state[2][2] in colors:
            return True
        if self.cube.bface.state[2][2] in colors and self.cube.lface.state[2][0] in colors and self.cube.dface.state[2][0] in colors:
            return True
        if self.cube.lface.state[2][2] in colors and self.cube.fface.state[0][2] in colors and self.cube.dface.state[0][0] in colors:
            return True
        return False

    def is_edge_in_bottom_layer(self) -> bool:
        '''Method used for looking for a piece in the bottom layer'''
        if self.cube.dface.state[2][1] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.dface.state[0][1] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.dface.state[1][0] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.dface.state[1][2] == self.cube.dface.state[1][1]:
            return True
        return False

    def is_edge_on_bottom_ring(self):
        '''Method used for looking for a piece in the bottom row of the f,r,b and l faces'''
        if self.cube.fface.state[2][1] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.rface.state[2][1] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.bface.state[2][1] == self.cube.dface.state[1][1]:
            return True
        elif self.cube.lface.state[2][1] == self.cube.dface.state[1][1]:
            return True
        return False

    def make_a_daisy(self):
        '''Starts with an unsolved cube, solves a daisy'''
        self.cube.moves += "Solving the daisy: "
        for i in range(4):
            if self.cube.uface.state[1][2] == self.cube.dface.state[1][1]:
                self.cube.Up()
            elif self.is_edge_in_bottom_layer():
                while self.cube.dface.state[1][2] != self.cube.dface.state[1][1]:
                    self.cube.D()
                self.cube.R2()
                self.cube.Up()
            elif self.cube.fface.state[1][2] == self.cube.dface.state[1][1]:
                self.cube.R()
                self.cube.Up()
            elif self.cube.fface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.U2()
                self.cube.Lp()
                self.cube.U()
            elif self.cube.rface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.U()
                self.cube.Fp()
                self.cube.U2()
            elif self.cube.rface.state[1][2] == self.cube.dface.state[1][1]:
                self.cube.Up()
                self.cube.B()
            elif self.cube.bface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.Rp()
                self.cube.Up()
            elif self.cube.bface.state[1][2] == self.cube.dface.state[1][1]:
                self.cube.U2()
                self.cube.L()
                self.cube.U()
            elif self.cube.lface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.Up()
                self.cube.Bp()
            elif self.cube.lface.state[1][2] == self.cube.dface.state[1][1]:
                self.cube.U()
                self.cube.F()
                self.cube.U2()
            elif self.is_edge_on_bottom_ring():
                while self.cube.fface.state[2][1] != self.cube.dface.state[1][1]:
                    self.cube.D()
                self.cube.U()
                self.cube.Fp()
                self.cube.Up()
                self.cube.R()
                self.cube.Up()
            elif self.cube.rface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.R()
                self.cube.Up()
                self.cube.B()
            elif self.cube.bface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.Bp()
                self.cube.Rp()
                self.cube.Up()
            elif self.cube.lface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.L()
                self.cube.U()
                self.cube.F()
                self.cube.U2()
            elif self.cube.fface.state[1][0] == self.cube.dface.state[1][1]:
                self.cube.F()
                self.cube.R()
                self.cube.Up()
            

    def daisy_to_cross(self):
        '''Starts with a daisy, solves the cross on the first face'''
        self.cube.moves += "\n Solving the cross on the bottom: "
        for i in range(4):
            while self.cube.fface.state[0][1] != self.cube.fface.state[1][1] or self.cube.uface.state[2][1] != self.cube.dface.state[1][1]:
                self.cube.U()
            self.cube.F2()
            self.cube.y()

    def corners_bottom_layer(self):
        '''Solves the corners in the bottom layer'''
        self.cube.moves += "\n Solving the bottom layer corners:"
        for i in range(4):
            colors = [self.cube.fface.state[1][1],
                      self.cube.dface.state[1][1], self.cube.rface.state[1][1]]
            if self.cube.fface.state[2][2] == self.cube.fface.state[1][1] and self.cube.dface.state[0][2] == self.cube.dface.state[1][1] and self.cube.rface.state[2][0] == self.cube.rface.state[1][1]:
                self.cube.y()
            elif self.is_corner_in_bottom_layer(colors):
                correctcorner = False
                while not correctcorner:
                    if self.cube.fface.state[2][2] in colors and self.cube.rface.state[2][0] in colors and self.cube.dface.state[0][2] in colors:
                        correctcorner = True
                        self.sexy_move()
                    else:
                        self.cube.D()
                realigned = False
                while not realigned:
                    if self.cube.fface.state[1][1] == self.cube.fface.state[2][1]:
                        realigned = True
                    else:
                        self.cube.D()
                if self.cube.fface.state[0][2] == self.cube.dface.state[1][1]:
                    self.reverse_sexy_move()
                elif self.cube.rface.state[0][0] == self.cube.dface.state[1][1]:
                    self.cube.R()
                    self.cube.U()
                    self.cube.Rp()
                else:
                    self.cube.R()
                    self.cube.U2()
                    self.cube.Rp()
                    self.cube.Up()
                    self.cube.R()
                    self.cube.U()
                    self.cube.Rp()
                self.cube.y()
            else:
                correctcorner = False
                while not correctcorner:
                    if self.cube.fface.state[0][2] in colors and self.cube.rface.state[0][0] in colors and self.cube.uface.state[2][2] in colors:
                        correctcorner = True
                        if self.cube.fface.state[0][2] == self.cube.dface.state[1][1]:
                            self.reverse_sexy_move()
                        elif self.cube.rface.state[0][0] == self.cube.dface.state[1][1]:
                            self.cube.R()
                            self.cube.U()
                            self.cube.Rp()
                        else:
                            self.cube.R()
                            self.cube.U2()
                            self.cube.Rp()
                            self.cube.Up()
                            self.cube.R()
                            self.cube.U()
                            self.cube.Rp()
                    else:
                        self.cube.U()
                self.cube.y()


    def find_and_insert_f2l(self, colors):
        '''This method finds the correct edge piece for the
        given F2l case and inserts it in the correct slot'''
        self.cube.moves += "Looking for F2L piece in top layer: "
        found_piece = False
        while not found_piece:
            if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
                found_piece = True
                if self.cube.fface.state[0][1] == self.cube.fface.state[1][1]:
                    self.insert_f2l_right()
                else:
                    self.cube.y()
                    self.cube.Up()
                    self.insert_f2l_left()
                    self.cube.yp()
            else:
                self.cube.U()

    def remove_f2l_from_wrong_slot(self, colors):
        '''Sometimes, an edge piece can be "stuck" in the wrong slot when solvign the F2L. This method allows to remove
        it from there and put it back into the top layer, from where it can be solved'''
        self.cube.moves += "Removing from wrong slot: "
        removed = False
        count = 0
        center = self.cube.fface.state[1][1]
        while not removed:
            count += 1
            if self.cube.fface.state[1][2] in colors and self.cube.rface.state[1][0] in colors:
                self.insert_f2l_right()
                removed = True
                while self.cube.fface.state[1][1] != center:
                    self.cube.y()
            else:
                self.cube.y()

    def solve_f2l(self):
        '''This method start with a solved first layer and solves the middle layer'''
        self.cube.moves += "\n Solving the second layer: "
        # check if this step is necessary
        if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.fface.state[1][0] == self.cube.fface.state[1][1] and self.cube.lface.state[1][2] == self.cube.lface.state[1][1] and self.cube.lface.state[1][0] == self.cube.lface.state[1][1] and self.cube.rface.state[1][2] == self.cube.rface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1] and self.cube.bface.state[1][2] == self.cube.bface.state[1][1] and self.cube.bface.state[1][0] == self.cube.bface.state[1][1]:
            return
        for i in range(4):
            colors = [self.cube.fface.state[1][1], self.cube.rface.state[1][1]]
            if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1]:
                self.cube.y()
            elif self.is_edge_in_top_layer(colors):
                self.find_and_insert_f2l(colors)
                self.cube.y()
            else:
                self.remove_f2l_from_wrong_slot(colors)
                self.find_and_insert_f2l(colors)
                self.cube.y()

    def solve_cross(self):
        '''This method starts with the first two layers of the cube solved and creates a cross on the top layer'''
        # check if this step is necessary
        self.cube.moves += "\n Solving the cross: "
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1] and self.cube.uface.state[1][0] == self.cube.uface.state[1][1] and self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
            return
        if self.cube.uface.state[0][1] != self.cube.uface.state[1][1] and self.cube.uface.state[1][0] != self.cube.uface.state[1][1] and self.cube.uface.state[1][2] != self.cube.uface.state[1][1]:
            self.make_a_cross()
            self.cube.U2()
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1]:
            if self.cube.uface.state[2][1] == self.cube.uface.state[1][1]:
                self.cube.Up()
                self.make_a_cross()
                return
            elif self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                self.make_a_cross()
                self.make_a_cross()
                return
            else:
                self.cube.U()
                self.make_a_cross()
                self.make_a_cross()
        else:
            if self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                if self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
                    self.make_a_cross()
                else:
                    self.cube.U()
                    self.make_a_cross()
                    self.make_a_cross()
            else:
                self.cube.U2()
                self.make_a_cross()
                self.make_a_cross()

    def adjust_cross(self):
        '''This method starts with a cross on the top layer and the first two layers solved. This method moves the edges all into their final positions. After this, the edges are fully solved'''
        self.cube.moves += "\n Aligning the cross: "
        # check if this step is necessary
        checks = 0
        while checks < 4:
            if self.cube.fface.state[0][1] == self.cube.fface.state[1][1] and self.cube.rface.state[0][1] == self.cube.rface.state[1][1] and self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                return
            self.cube.U()
            checks += 1
        aligned = False
        count = 0
        while not aligned:
            self.cube.U()
            count += 1
            numberofpiecesaligned = 0
            if self.cube.fface.state[0][1] == self.cube.fface.state[1][1]:
                numberofpiecesaligned += 1
            if self.cube.rface.state[0][1] == self.cube.rface.state[1][1]:
                numberofpiecesaligned += 1
            if self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                numberofpiecesaligned += 1
            if self.cube.lface.state[0][1] == self.cube.lface.state[1][1]:
                numberofpiecesaligned += 1
            if numberofpiecesaligned == 2:
                aligned = True

        if self.cube.fface.state[0][1] != self.cube.fface.state[1][1]:
            if self.cube.bface.state[0][1] != self.cube.bface.state[1][1]:
                self.move_cross_pieces()
                self.cube.U()
                self.cube.y()
                self.move_cross_pieces()

            elif self.cube.rface.state[0][1] != self.cube.rface.state[1][1]:
                self.cube.y()
                self.move_cross_pieces()
            else:
                self.move_cross_pieces()
        else:
            if self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                self.move_cross_pieces()
                self.adjust_cross()
            elif self.cube.rface.state[0][1] == self.cube.rface.state[1][1]:
                self.cube.yp()
                self.move_cross_pieces()
            else:
                self.cube.y2()
                self.move_cross_pieces()

    def move_corners(self):
        '''This method start with a cube with the first two layers 
        and the cross on the top face solved and adjusted,
        and moves the corners into the correct spots. 
        After this, they will only need to be rotated.'''
        self.cube.moves += "\n Getting the corners in the right positions: "
        corners_checked = 0
        # check if performing this step is needed
        if self.is_top_right_corner_correct():
            self.cube.yp()
            if self.is_top_right_corner_correct():
                self.cube.y()
                return
            else:
                self.cube.y()
                found_correct = True
            # this part of the if works
        else:
            found_correct = False
            while corners_checked < 4 and not found_correct:
                self.cube.y()
                if self.is_top_right_corner_correct():
                    found_correct = True
                corners_checked += 1
        if found_correct:
            self.move_corners_clockwise()
            self.cube.y()
            if self.is_top_right_corner_correct():
                self.cube.yp()
                return
            self.cube.yp()
            self.move_corners_clockwise()
            return
        else:
            self.move_corners_clockwise()
            self.move_corners()

    def rotate_corners(self):
        '''This method rotates each corner. After this method, the cube will be solved'''
        self.cube.moves += "\n Rotating the corners: "
        # first check if corners are already rotated correctly
        self.cube.z2()
        if self.cube.fface.state[2][2] == self.cube.fface.state[1][1] and self.cube.fface.state[2][0] == self.cube.fface.state[1][1] and self.cube.rface.state[2][2] == self.cube.rface.state[1][1]:
            return
        corners = 0
        while corners < 4:
            if self.cube.dface.state[0][2] == self.cube.dface.state[1][1]:
                self.cube.D()
            elif self.cube.rface.state[2][0] == self.cube.dface.state[1][1]:
                self.sexy_move()
                self.sexy_move()
                self.cube.D()
            else:
                self.reverse_sexy_move()
                self.reverse_sexy_move()
                self.cube.D()
            corners += 1

    def solve(self):
        '''Main method of the solver class'''
        print("Solving the daisy")
        self.make_a_daisy()
        self.cube.show_cube()
        print("Solving the cross on the bottom")
        self.daisy_to_cross()
        self.cube.show_cube()
        print(self.cube.moves)
        print("Solving bottom corners")
        self.corners_bottom_layer()
        print("solve f2l")
        self.solve_f2l()
        print("cross")
        self.solve_cross()
        print("adjust cross")
        self.adjust_cross()
        print("move corners")
        self.move_corners()
        print("rotate corners")
        self.rotate_corners()
        self.cube.moves += "Solved!"
        print(self.cube.moves)
