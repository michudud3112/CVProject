import Face
import cube
class solver:
    def __init__(self,cube,solution) -> None:
        self.cube = cube
        self.solution = solution
    
    #some useful algorithms
    def sexymove(self):
        self.cube.R()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()
        self.solution += "R U R' U' "
    
    def reversesexymove(self):
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
        self.solution += "U R U' R' "
        
    def movecornersclockwise(self):
        self.cube.Lp()
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.L()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()
        self.solution += "L' U R U' L U R' U' "
                
    def movecrosspieces(self):
        self.cube.Up()
        self.cube.R()
        self.cube.U2()
        self.cube.Rp()
        self.cube.Up()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
        self.solution += "U' R U2 R' U' R U' R' "
    
    def makeacross(self):
        self.cube.F()
        self.solution += "F "
        self.sexymove()
        self.cube.Fp()
        self.solution += "F' "
    
    def insertF2Lleft(self):
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
        self.solution += "inserting left: "
        self.solution += "U' L' U L y' U R U' R' y "

    def insertF2Lright(self):
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
        self.solution += "inserting right: "
        self.solution += "U R U' R' y U' L' U L y'"
    
    #some checking methods
    def istoprightcornercorrect(self) -> bool:
        if self.cube.uface.state[2][2] == self.cube.uface.state[1][1] and self.cube.fface.state[0][2] == self.cube.fface.state[1][1] and self.cube.rface.state[0][0] == self.cube.rface.state[1][1]:
            return True
        elif self.cube.uface.state[2][2] == self.cube.rface.state[1][1] and self.cube.fface.state[0][2] == self.cube.uface.state[1][1] and self.cube.rface.state[0][0] == self.cube.fface.state[1][1]:
            return True
        elif self.cube.uface.state[2][2] == self.cube.fface.state[1][1] and self.cube.fface.state[0][2] == self.cube.rface.state[1][1] and self.cube.rface.state[0][0] == self.cube.uface.state[1][1]:
            return True
        else:
            return False
    
    def ispieceintoplayer(self, colors) -> bool:
        if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
            return True
        if self.cube.lface.state[0][1] in colors and self.cube.uface.state[1][0] in colors:
            return True
        if self.cube.rface.state[0][1] in colors and self.cube.uface.state[1][2] in colors:
            return True
        if self.cube.bface.state[0][1] in colors and self.cube.uface.state[0][1] in colors :
            return True
        return False
        
    def makedaisy(self):
        self.solution += "Solving the daisy: "
        self.cube.y()
    
    def daisytocross(self):
        self.solution += "Solving the cross on the bottom: "
        for i in range(4):
            while self.cube.fface.state[0][1] != self.cube.fface.state[1][1]:
                self.cube.U()
                self.solution += "U "
            self.cube.F2()
            self.solution += "F2 "
            self.cube.y()
            self.solution += "y "
        
    
    def cornersbottomlayer(self):
        self.solution += "Solving the bottom layer corners:"
        self.cube.y()
        
    def findandinsertF2L(self,colors):
        foundPiece = False
        while not foundPiece:
            self.cube.U()
            self.solution += "U "
            if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
                foundPiece = True
                if self.cube.fface.state[0][1] == self.cube.fface.state[1][1]:
                    self.insertF2Lright()
                else:
                    self.solution += "y U' "
                    self.cube.y()
                    self.cube.Up()
                    self.insertF2Lleft()
                    self.cube.yp()
                    self.solution += "y' "
        
    def removeF2Lfromwrongslot(self,colors):
        removed = False
        count = 0
        while not removed:
            self.cube.y()
            count += 1
            self.solution += "y "
            if self.cube.fface.state[1][2] in colors and self.cube.rface.state[1][0] in colors:
                self.insertF2Lright()
                removed = True
                for i in range(count):
                    self.cube.yp()
                    self.solution += "y' "
        
    def solveF2L(self):
        self.solution += "Solving the second layer: "
        #check if this step is necessary
        if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.fface.state[1][0] == self.cube.fface.state[1][1] and self.cube.lface.state[1][2] == self.cube.lface.state[1][1] and self.cube.lface.state[1][0] == self.cube.lface.state[1][1] and self.cube.rface.state[1][2] == self.cube.rface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1] and self.cube.bface.state[1][2] == self.cube.bface.state[1][1] and self.cube.bface.state[1][0] == self.cube.bface.state[1][1]:
            return
        for i in range(4):
            colors = [self.cube.fface.state[1][1],self.cube.rface.state[1][1]]
            if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1]:
                self.cube.y()
                self.solution += "y "
            elif self.ispieceintoplayer(colors):
                self.findandinsertF2L(colors)
            else:
               self.removeF2Lfromwrongslot(colors)
               self.findandinsertF2L(colors) 
            self.cube.y()
            self.solution += "y "
    
    def solvecross(self):
        #check if this step is necessary
        self.solution += "Solving the cross: "
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1] and self.cube.uface.state[1][0] == self.cube.uface.state[1][1] and self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
            return
        if self.cube.uface.state[0][1] != self.cube.uface.state[1][1] and self.cube.uface.state[1][0] != self.cube.uface.state[1][1] and self.cube.uface.state[1][2] != self.cube.uface.state[1][1]: 
            self.makeacross()
            self.cube.U2()
            self.solution += "U2 "
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1]:
            if self.cube.uface.state[2][1] == self.cube.uface.state[1][1]:
                self.cube.Up()
                self.solution += "U' "
                self.makeacross()
                return
            elif self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                self.makeacross()
                self.makeacross()
                return
            else:
                self.cube.U()
                self.solution += "U' "
                self.makeacross()
                self.makeacross()
        else:
            if self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                if self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
                    self.makeacross()
                else:
                    self.cube.U()
                    self.solution += "U "
                    self.makeacross()
                    self.makeacross()
            else:
                self.cube.U2()
                self.solution += "U2 "
                self.makeacross()
                self.makeacross()
        
    def adjustcross(self):
        self.solution += "Aligning the cross: "
        #check if this step is necessary
        checks = 0
        while checks < 4:
            if self.cube.fface.state[0][1] == self.cube.fface.state[1][1] and self.cube.rface.state[0][1] == self.cube.rface.state[1][1] and self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                if checks == 1:
                    self.solution += "U "
                elif checks == 2:
                    self.solution += "U2 "
                elif checks == 3:
                    self.solution += "U' "
                return
            self.cube.U()
            checks +=1
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
        if count == 1:
            self.solution += "U "
        elif count == 2:
            self.solution += "U2 "
        elif count == 3:
            self.solution += "U' "
        
        if self.cube.fface.state[0][1] != self.cube.fface.state[1][1]:
            if self.cube.bface.state[0][1] != self.cube.bface.state[1][1]:
                self.movecrosspieces()
                self.cube.U()
                self.cube.y()
                self.solution += "U y "
                self.movecrosspieces()
                
            elif self.cube.rface.state[0][1] != self.cube.rface.state[1][1]:
                self.cube.y()
                self.solution += "y "
                self.movecrosspieces()
            else:
                self.movecrosspieces()
        else:
            if self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                self.movecrosspieces()
                self.adjustcross()
            elif self.cube.rface.state[0][1] == self.cube.rface.state[1][1]:
                self.cube.yp()
                self.solution += "y' "
                self.movecrosspieces()
            else:
                self.cube.y2()
                self.solution += "y2 "
                self.movecrosspieces()
                    
    def movecorners(self):
        self.solution += "Getting the corners in the right positions: "
        cornersChecked = 0
        #check if performing this step is needed
        if self.istoprightcornercorrect():
            self.cube.yp()
            if self.istoprightcornercorrect():
                self.cube.y()
                return
            else:
                self.cube.y()
                foundCorrect = True
            #this part of the if works
        else:
            foundCorrect = False
            while cornersChecked < 4 and not foundCorrect:
                self.cube.y()
                if self.istoprightcornercorrect():
                    foundCorrect = True
                cornersChecked += 1
        if foundCorrect:
            if cornersChecked == 1:
                self.solution += "y "
            elif cornersChecked == 2:
                self.solution += "y2 "
            elif cornersChecked == 3:
                self.solution += "y' "
            self.movecornersclockwise()
            self.cube.y()
            if self.istoprightcornercorrect():
                self.cube.yp()
                return
            else:
                self.cube.yp()
                self.movecornersclockwise()
                return
        else:
            self.movecornersclockwise()
            self.movecorners()
        
    def rotatecorners(self):
        self.solution += "Rotating the corners: " 
        #first check if corners are already rotated correctly
        self.cube.z2()
        if self.cube.fface.state[2][2] == self.cube.fface.state[1][1] and self.cube.fface.state[2][0] == self.cube.fface.state[1][1] and self.cube.rface.state[2][2] == self.cube.rface.state[1][1]:
            return
        corners = 0
        self.solution += "z2 "
        while corners <4:
            if self.cube.dface.state[0][2] == self.cube.dface.state[1][1]:
                self.cube.D()
                self.solution += "D "
            elif self.cube.rface.state[2][0] == self.cube.dface.state[1][1]:
                self.sexymove()
                self.sexymove()
                self.cube.D()
                self.solution += "D "
            else:
                self.reversesexymove()
                self.reversesexymove()
                self.cube.D()
                self.solution += "D "
            corners += 1

    
    def solve(self): 
        self.solveF2L()
        self.solvecross()
        self.adjustcross()
        self.movecorners()
        self.rotatecorners()
        self.solution += "Solved!"
        print(self.solution)
    
        