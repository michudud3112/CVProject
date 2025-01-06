class labels:
    #!!!important!!!
    #labels: 1 top, 2 left, 3 front, 5 right, 4 back, 6 bottom assuming smallest side on bottom
    def __init__(self, grid, depth, alpha):
        self.grid = grid
        self.alpha = alpha  # hyperparameter for error tolerance, recommend default 0.1
        self.cube_ratios = [1.625, 1.375, 0.875, 1.125, 0.625, 0.375]
        self.depth = depth
        self.labels =[[[0,0,0],[0,0,0],[0,0,0]],
                      [[0,0,0],[0,0,0],[0,0,0]],
                      [[0,0,0],[0,0,0],[0,0,0]],
                      [[0,0,0],[0,0,0],[0,0,0]],
                      [[0,0,0],[0,0,0],[0,0,0]],
                      [[0,0,0],[0,0,0],[0,0,0]]]

    def calculate_ratios(self, index):
        ratios = []
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    ratios[i][j][k] = self.grid[index][i][j][k] / \
                        self.grid[index][2][2][k]  # scaling by the center
        self.grid[index] = ratios

    def ratios_to_labels(self):
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    ratio = self.grid[i][j][k][0]
                    for m in range(6):
                        if abs(ratio-self.cube_ratios[m]) < self.alpha:
                            self.grid[i][j][k][0] = m+1
                    ratio = self.grid[i][j][k][1]
                    for m in range(6):
                        if abs(ratio-self.cube_ratios[m]) < self.alpha:
                            self.grid[i][j][k][1] = m+1

    def match_labels_to_pieces_top_layer(self):
        self.labels[0][0][0] = self.grid[1][0][0][1]
        self.labels[0][0][1] = self.grid[4][0][1][1]
        self.labels[0][0][2] = self.grid[3][0][2][1]
        self.labels[0][1][0] = self.grid[1][0][1][1]
        self.labels[0][1][2] = self.grid[3][0][1][1]
        self.labels[0][2][0] = self.grid[1][0][2][1]
        self.labels[0][2][1] = self.grid[2][0][1][1]
        self.labels[0][2][2] = self.grid[3][0][2][0]
    
    def match_labels_to_pieces_left_layer(self):
        self.labels[1][0][0] = self.grid[4][0][2][0]
        self.labels[1][0][1] = self.grid[0][1][0][0]
        self.labels[1][0][2] = self.grid[2][0][0][0]
        self.labels[1][1][0] = self.grid[4][1][2][0]
        self.labels[1][1][2] = self.grid[2][1][0][0]
        self.labels[1][2][0] = self.grid[4][2][2][0]
        self.labels[1][2][1] = self.grid[5][1][0][0]
        self.labels[1][2][2] = self.grid[2][2][0][0]
    
    def match_labels_to_pieces_front_layer(self):
        self.labels[2][0][0] = self.grid[0][2][0][1]
        self.labels[2][0][1] = self.grid[0][2][1][1]
        self.labels[2][0][2] = self.grid[0][2][2][1]
        self.labels[2][1][0] = self.grid[1][1][2][0]
        self.labels[2][1][2] = self.grid[3][1][0][0]
        self.labels[2][2][0] = self.grid[5][0][0][1]
        self.labels[2][2][1] = self.grid[5][0][1][1]
        self.labels[2][2][2] = self.grid[5][0][2][1]

    def match_labels_to_pieces_right_layer(self):
        self.labels[3][0][0] = self.grid[2][0][2][0]
        self.labels[3][0][1] = self.grid[0][1][2][0]
        self.labels[3][0][2] = self.grid[4][0][0][0]
        self.labels[3][1][0] = self.grid[2][1][2][0]
        self.labels[3][1][2] = self.grid[4][1][0][0]
        self.labels[3][2][0] = self.grid[2][2][2][0]
        self.labels[3][2][1] = self.grid[5][1][2][0]
        self.labels[3][2][2] = self.grid[4][2][0][0]
    
    def match_labels_to_pieces_back_layer(self):
        self.labels[4][0][0] = self.grid[0][0][2][1]
        self.labels[4][0][1] = self.grid[0][0][1][1]
        self.labels[4][0][2] = self.grid[0][0][0][1]
        self.labels[4][1][0] = self.grid[3][1][2][0]
        self.labels[4][1][2] = self.grid[1][1][0][0]
        self.labels[4][2][0] = self.grid[5][2][2][1]
        self.labels[4][2][1] = self.grid[5][2][1][1]
        self.labels[4][2][2] = self.grid[5][2][0][1]
      
    def match_labels_to_pieces_down_layer(self):
        self.labels[5][0][0] = self.grid[2][2][0][1]
        self.labels[5][0][1] = self.grid[2][2][1][1]
        self.labels[5][0][2] = self.grid[2][2][2][1]
        self.labels[5][1][0] = self.grid[1][2][1][1]
        self.labels[5][1][2] = self.grid[3][2][1][1]
        self.labels[5][2][0] = self.grid[4][2][2][1]
        self.labels[5][2][1] = self.grid[4][2][1][1]
        self.labels[5][2][2] = self.grid[4][2][0][1]
        
    def center_labels(self):
        #top label
        height = self.grid[4][0][1][1]
        height += self.depth[0][1]-self.depth[0][4]
        for m in range(6):
            if abs(height-self.cube_ratios[m]) < self.alpha:
                self.labels[0][1][1] = m+1
        #left label
        height = self.grid[0][1][0][0]
        height += self.depth[1][1]-self.depth[1][4]
        for m in range(6):
            if abs(height-self.cube_ratios[m]) < self.alpha:
                self.labels[1][1][1] = m+1
        
        #front label
        height = self.grid[0][2][1][1]
        height += self.depth[2][1]-self.depth[2][4]
        for m in range(6):
            if abs(height-self.cube_ratios[m]) < self.alpha:
                self.labels[2][1][1] = m+1
        
        self.labels[3][1][1] = 7 -self.labels[1][1][1]            
        self.labels[4][1][1] = 7 -self.labels[2][1][1]
        self.labels[5][1][1] = 7 -self.labels[0][1][1]        
        
    def return_labels(self):
        return self.labels
    
    def calculate_labels(self):
        for i in range(len(self.grid)):
            self.calculate_ratios(i)
        self.ratios_to_labels()
        self.match_labels_to_pieces_top_layer()
        self.match_labels_to_pieces_left_layer()
        self.match_labels_to_pieces_front_layer()
        self.match_labels_to_pieces_right_layer()
        self.match_labels_to_pieces_back_layer()
        self.match_labels_to_pieces_down_layer()
        self.center_labels()
        self.return_labels()
        
