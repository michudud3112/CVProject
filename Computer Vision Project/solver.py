import Face
import cube
class solver:
    def __init__(self,cube) -> None:
        self.cube = cube
    
    #some useful algorithms
    def sexymove(self):
        self.cube.R()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()
    
    def reversesexymove(self):
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
        
    def movecornersclockwise(self):
        self.cube.Lp()
        self.cube.U()
        self.cube.R()
        self.cube.Up()
        self.cube.L()
        self.cube.U()
        self.cube.Rp()
        self.cube.Up()
                
    def movecrosspieces(self):
        self.cube.Up()
        self.cube.R()
        self.cube.U2()
        self.cube.Rp()
        self.cube.Up()
        self.cube.R()
        self.cube.Up()
        self.cube.Rp()
    
    def makeacross(self):
        self.cube.F()
        self.sexymove()
        self.cube.Fp()
    
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
    
    def isedgeintoplayer(self, colors) -> bool:
        if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
            return True
        if self.cube.lface.state[0][1] in colors and self.cube.uface.state[1][0] in colors:
            return True
        if self.cube.rface.state[0][1] in colors and self.cube.uface.state[1][2] in colors:
            return True
        if self.cube.bface.state[0][1] in colors and self.cube.uface.state[0][1] in colors :
            return True
        return False
    
    def iscornerinbottomlayer(self,colors):
        if self.cube.fface.state[2][2] in colors and self.cube.rface.state[2][0] in colors and self.cube.dface.state[0][2] in colors:
            return True
        if self.cube.rface.state[2][2] in colors and self.cube.bface.state[2][0] in colors and self.cube.dface.state[2][2] in colors:
            return True
        if self.cube.bface.state[2][2] in colors and self.cube.lface.state[2][0] in colors and self.cube.dface.state[2][0] in colors:
            return True
        if self.cube.lface.state[2][2] in colors and self.cube.fface.state[0][2] in colors and self.cube.dface.state[0][0] in colors:
            return True
        return False
        
    def makedaisy(self):
        self.cube.moves += "Solving the daisy: "
        self.cube.y()
    
    def daisytocross(self):
        self.cube.moves += "Solving the cross on the bottom: "
        for i in range(4):
            while self.cube.fface.state[0][1] != self.cube.fface.state[1][1]:
                self.cube.U()
            self.cube.F2()
            self.cube.y()
        
    
    def cornersbottomlayer(self):
        self.cube.moves += "Solving the bottom layer corners:"
        for i in range(4):
            colors = [self.cube.fface.state[1][1],self.cube.dface.state[1][1],self.cube.rface.state[1][1]]
            if self.cube.fface.state[2][2] == self.cube.fface.state[1][1] and self.cube.dface.state[0][2] == self.cube.dface.state[1][1] and self.cube.rface.state[2][0] == self.cube.rface.state[1][1]:
                self.cube.y()
            elif self.iscornerinbottomlayer(colors):
                correctcorner = False
                while not correctcorner:
                    if self.cube.fface.state[2][2] in colors and self.cube.rface.state[2][0] in colors and self.cube.dface.state[0][2] in colors:
                        correctcorner = True
                        self.sexymove()
                    else:
                        self.cube.D()
                realigned = False
                while not realigned:
                    if self.cube.fface.state[1][1] == self.cube.fface.state[2][1]:
                        realigned = True
                    else:
                        self.cube.D()
                if self.cube.fface.state[0][2] == self.cube.dface.state[1][1]:
                    self.reversesexymove()
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
                            self.reversesexymove()
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
                        self.cube.U()
                
        
    def findandinsertF2L(self,colors):
        foundPiece = False
        while not foundPiece:
            self.cube.U()
            if self.cube.fface.state[0][1] in colors and self.cube.uface.state[2][1] in colors:
                foundPiece = True
                if self.cube.fface.state[0][1] == self.cube.fface.state[1][1]:
                    self.insertF2Lright()
                else:
                    self.cube.y()
                    self.cube.Up()
                    self.insertF2Lleft()
                    self.cube.yp()
        
    def removeF2Lfromwrongslot(self,colors):
        removed = False
        count = 0
        center = self.cube.fface.state[1][1]
        while not removed:
            self.cube.y()
            count += 1
            if self.cube.fface.state[1][2] in colors and self.cube.rface.state[1][0] in colors:
                self.insertF2Lright()
                removed = True
                while self.cube.fface.state[1][1] != center:               
                    self.cube.yp()
        
    def solveF2L(self):
        self.cube.moves += "Solving the second layer: "
        print("Solving f2l")
        #check if this step is necessary
        if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.fface.state[1][0] == self.cube.fface.state[1][1] and self.cube.lface.state[1][2] == self.cube.lface.state[1][1] and self.cube.lface.state[1][0] == self.cube.lface.state[1][1] and self.cube.rface.state[1][2] == self.cube.rface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1] and self.cube.bface.state[1][2] == self.cube.bface.state[1][1] and self.cube.bface.state[1][0] == self.cube.bface.state[1][1]:
            return
        for i in range(4):
            colors = [self.cube.fface.state[1][1],self.cube.rface.state[1][1]]
            if self.cube.fface.state[1][2] == self.cube.fface.state[1][1] and self.cube.rface.state[1][0] == self.cube.rface.state[1][1]:
                self.cube.y()
            elif self.isedgeintoplayer(colors):
                self.findandinsertF2L(colors)
                self.cube.y()
            else:
                self.removeF2Lfromwrongslot(colors)
                self.findandinsertF2L(colors) 
                self.cube.y()
            
    
    def solvecross(self):
        #check if this step is necessary
        self.cube.moves += "Solving the cross: "
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1] and self.cube.uface.state[1][0] == self.cube.uface.state[1][1] and self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
            return
        if self.cube.uface.state[0][1] != self.cube.uface.state[1][1] and self.cube.uface.state[1][0] != self.cube.uface.state[1][1] and self.cube.uface.state[1][2] != self.cube.uface.state[1][1]: 
            self.makeacross()
            self.cube.U2()
        if self.cube.uface.state[0][1] == self.cube.uface.state[1][1]:
            if self.cube.uface.state[2][1] == self.cube.uface.state[1][1]:
                self.cube.Up()
                self.makeacross()
                return
            elif self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                self.makeacross()
                self.makeacross()
                return
            else:
                self.cube.U()
                self.makeacross()
                self.makeacross()
        else:
            if self.cube.uface.state[1][0] == self.cube.uface.state[1][1]:
                if self.cube.uface.state[1][2] == self.cube.uface.state[1][1]:
                    self.makeacross()
                else:
                    self.cube.U()
                    self.makeacross()
                    self.makeacross()
            else:
                self.cube.U2()
                self.makeacross()
                self.makeacross()
        
    def adjustcross(self):
        self.cube.moves += "Aligning the cross: "
        #check if this step is necessary
        checks = 0
        while checks < 4:
            if self.cube.fface.state[0][1] == self.cube.fface.state[1][1] and self.cube.rface.state[0][1] == self.cube.rface.state[1][1] and self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
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
        
        if self.cube.fface.state[0][1] != self.cube.fface.state[1][1]:
            if self.cube.bface.state[0][1] != self.cube.bface.state[1][1]:
                self.movecrosspieces()
                self.cube.U()
                self.cube.y()
                self.movecrosspieces()
                
            elif self.cube.rface.state[0][1] != self.cube.rface.state[1][1]:
                self.cube.y()
                self.movecrosspieces()
            else:
                self.movecrosspieces()
        else:
            if self.cube.bface.state[0][1] == self.cube.bface.state[1][1]:
                self.movecrosspieces()
                self.adjustcross()
            elif self.cube.rface.state[0][1] == self.cube.rface.state[1][1]:
                self.cube.yp()
                self.movecrosspieces()
            else:
                self.cube.y2()
                self.movecrosspieces()
                    
    def movecorners(self):
        self.cube.moves += "Getting the corners in the right positions: "
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
        self.cube.moves += "Rotating the corners: " 
        #first check if corners are already rotated correctly
        self.cube.z2()
        if self.cube.fface.state[2][2] == self.cube.fface.state[1][1] and self.cube.fface.state[2][0] == self.cube.fface.state[1][1] and self.cube.rface.state[2][2] == self.cube.rface.state[1][1]:
            return
        corners = 0
        while corners <4:
            if self.cube.dface.state[0][2] == self.cube.dface.state[1][1]:
                self.cube.D()
            elif self.cube.rface.state[2][0] == self.cube.dface.state[1][1]:
                self.sexymove()
                self.sexymove()
                self.cube.D()
            else:
                self.reversesexymove()
                self.reversesexymove()
                self.cube.D()
            corners += 1

    
    def solve(self):
        self.daisytocross()
        self.cornersbottomlayer() 
        self.solveF2L()
        self.solvecross()
        self.adjustcross()
        self.movecorners()
        self.rotatecorners()
        self.cube.moves += "Solved!"
        print(self.cube.moves)
    
        