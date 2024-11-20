class face:
    def __init__(self, state) -> None:
        self.state = state
    def rotate_clockwise(self):
        '''This method enables a face to rotate 90 degrees (one turn) clockwise around itself'''
        #rotate the corners
        temp = self.state[0][0]
        self.state[0][0],self.state[2][0],self.state[2][2],self.state[0][2] = self.state[2][0],self.state[2][2],self.state[0][2],temp
        #rotate the edges
        temp = self.state[0][1]
        self.state[0][1],self.state[1][0],self.state[2][1],self.state[1][2] = self.state[1][0],self.state[2][1],self.state[1][2],temp
        
        #no need to rotate the centers
        
    def rotate_counterclockwise(self):
        '''This method enables a face to rotate 90 degrees (one turn) counterclockwise around itself'''
        #rotate corners
        temp = self.state[0][0]
        self.state[0][0],self.state[0][2],self.state[2][2], self.state[2][0] = self.state[0][2],self.state[2][2], self.state[2][0],temp
        #rotate the edges
        temp = self.state[0][1]
        self.state[0][1],self.state[1][2],self.state[2][1],self.state[1][0] = self.state[1][2],self.state[2][1],self.state[1][0],temp
        
    #I suppose I don't necessarily need this method but I immagine coding it like this might be more efficient
    def rotate_180(self):
        '''This method allows a face to rotate 180 degrees (two turns) around itself'''
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
    
    def show_face(self):
        '''Neatly displays the state of a face'''
        print(self.state[0][0], self.state[0][1],self.state[0][2])
        print(self.state[1][0], self.state[1][1],self.state[1][2])
        print(self.state[2][0], self.state[2][1],self.state[2][2])
        
       