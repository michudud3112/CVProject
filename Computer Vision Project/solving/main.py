import Solver
import Face
import Cube
# for testing - 1 is white, 2 is orange, 3 is green, 4 is red, 5 is blue, 6 is yellow

uface = Face.face([[3, 1, 1], [6, 6, 2], [4, 2, 5]])
lface = Face.face([[6, 3, 3], [2, 4, 5], [4, 1, 6]])
fface = Face.face([[6, 6, 2], [1, 3, 4], [4, 3, 5]])
rface = Face.face([[1, 3, 3], [5, 2, 4], [2, 6, 2]])
bface = Face.face([[4, 3, 2], [6, 5, 5], [1, 2, 5]])
dface = Face.face([[5, 4, 6], [4, 1, 5], [1, 1, 3]])

#this fails the test rn at the stage of solving the bottom layer corners Scramble: F2 L U2 L2 B2 L2 D F2 R2 U2 F2 D' L' U F R D L D F
#uface = Face.face([[4,2,6],[6,6,5],[6,4,3]])
#lface = Face.face([[3,2,5],[4,4,5],[5,1,1]])
#fface = Face.face([[4,6,2],[6,3,5],[2,1,1]])
#rface = Face.face([[6,4,4],[2,2,3],[3,3,5]])
#bface = Face.face([[3,3,1],[6,5,3],[4,2,6]])
#dface = Face.face([[5,5,2],[4,1,1],[2,1,1]])

#pieces with unique IDs to verify correctness of various moves
#uface = Face.face([[11,12,13],[14,15,16],[17,18,19]])
#lface = Face.face([[21,22,23],[24,25,26],[27,28,29]])
#fface = Face.face([[31,32,33],[34,35,36],[37,38,39]])
#rface = Face.face([[41,42,43],[44,45,46],[47,48,49]])
#bface = Face.face([[51,52,53],[54,55,56],[57,58,59]])
#dface = Face.face([[61,62,63],[64,65,66],[67,68,69]])
mycube = Cube.cube(uface,lface,fface,rface,bface,dface,"")
mysolver = Solver.solver(mycube)
mysolver.solve()
mycube.show_cube()
