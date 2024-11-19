class face:
    def __init__(self, state) -> None:
        self.state = state
    def rotateclockwise(self):
        #rotate the corners
        temp = self.state[0][0]
        self.state[0][0],self.state[2][0],self.state[2][2],self.state[0][2] = self.state[2][0],self.state[2][2],self.state[0][2],temp
        #rotate the edges
        temp = self.state[0][1]
        self.state[0][1],self.state[1][0],self.state[2][1],self.state[1][2] = self.state[1][0],self.state[2][1],self.state[1][2],temp
        
        #no need to rotate the centers
        
    def rotatecounterclockwise(self):
        #rotate corners
        temp = self.state[0][0]
        self.state[0][0],self.state[0][2],self.state[2][2], self.state[2][0] = self.state[0][2],self.state[2][2], self.state[2][0],temp
        #rotate the edges
        temp = self.state[0][1]
        self.state[0][1],self.state[1][2],self.state[2][1],self.state[1][0] = self.state[1][2],self.state[2][1],self.state[1][0],temp
        
    #I suppose I don't necessarily need this method but I immagine coding it like this might be more efficient
    def rotate180(self):
        #rotate corners
        temp = self.state[0][0]
        self.state[0][0],self.state[2][2] = self.state[2][2],temp
        temp = self.state[0][2]
        self.state[0][2],self.state[2][0] = self.state[2][0],temp
        
        #rotate the edges
        temp = self.state[0][1]
        self.state[0][1],self.state[2][1] = self.state[2][1],temp
        temp = self.state[1][0]
        self.state[1][0],self.state[1][2] = self.state[1][2],temp
    
    def showface(self):
        print(self.state[0][0], self.state[0][1],self.state[0][2])
        print(self.state[1][0], self.state[1][1],self.state[1][2])
        print(self.state[2][0], self.state[2][1],self.state[2][2])
        
       