import cube
import Face
import solver
import movecleaner
#when indexing: 0 top, 1 left, 2 front, 3 right, 4 back, 5 down


# for testing - 1 is white, 2 is orange, 3 is green, 4 is red, 5 is blue, 6 is yellow
# the bottom face (dface) is the one that gets solved first

#this is where the faces are predefined. these can be changed as long as the new cube is a valid cube
uface = Face.face([[4, 3, 2], [1, 6, 4], [1, 4, 2]])
lface = Face.face([[6, 2, 5], [6, 4, 5], [2, 4, 6]])
fface = Face.face([[2, 1, 5], [2, 3, 1], [4, 3, 1]])
rface = Face.face([[6, 5, 6], [5, 2, 3], [5, 2, 4]])
bface = Face.face([[3, 4, 3], [1, 5, 5], [3, 2, 3]])
dface = Face.face([[5, 6, 4], [6, 1, 3], [1, 6, 1]])


#this is where the face are added to the cube. Preferrably change the variables above
mycube = cube.cube(uface, lface, fface, rface, bface, dface, "", [])
mysolver = solver.Solver(mycube)
mysolver.solve()
print(mysolver.cube.solution)
mycube.show_cube()



#for i in range(len(mycube.moves)):
    #print("Direction:", mycube.moves[i].direction, "Count", mycube.moves[i].num)
# D' F2 L2 F2 U' F2 L2 D B2 D2 B2 F' U L' R' B2 D' L2 B L2 R'
# U R U2 F R2 B D2 L2 D2 U2 F D2 F' U' L D' F U F' R'


