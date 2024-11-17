import Solver
import Face
import Cube
# for testing - 1 is white, 2 is orange, 3 is green, 4 is red, 5 is blue, 6 is yellow
uface = Face.face([[4,1,5],[1,6,1],[2,1,6]])
lface = Face.face([[1,3,6],[6,4,5],[1,4,1]])
fface = Face.face([[4,5,2],[6,3,2],[3,2,4]])
rface = Face.face([[5,2,2],[3,2,2],[5,4,3]])
bface = Face.face([[1,4,5],[5,5,3],[6,4,3]])
dface = Face.face([[2,6,6],[5,1,3],[4,6 ,2]])

#use scramble below + fix daisy to achieve position below. 
#U2 B2 D' B2 D' R2 U' F2 U L2 B2 U' B D2 R B D L2 D U
#uface = Face.face([[2,1,2],[1,6,1],[2,1,5]])
#lface = Face.face([[5,3,3],[3,4,3],[4,6,3]])
#fface = Face.face([[1,5,1],[2,3,6],[1,5,5]])
#rface = Face.face([[4,4,5],[2,2,4],[6,4,3]])
#bface = Face.face([[6,2,1],[3,5,6],[6,5,3]])
#dface = Face.face([[4,4,4],[5,1,6],[6,2,2]])

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
