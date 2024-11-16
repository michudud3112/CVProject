import solver
import Face
import cube
#cube
# for testing - 1 is white, 2 is orange, 3 is green, 4 is red, 5 is blue, 6 is yellow
uface = Face.face([[2,1,1],[1,6,1],[3,1,6]])
lface = Face.face([[1,5,2],[5,4,4],[2,3,5]])
fface = Face.face([[6,3,2],[6,3,3],[4,5,4]])
rface = Face.face([[5,4,3],[4,2,6],[6,3,6]])
bface = Face.face([[4,2,3],[2,5,2],[4,5,1]])
dface = Face.face([[1,4,3],[2,1,6],[5,6,5]])

#pieces with unique IDs to verify correctness of various moves
#uface = Face.face([[11,12,13],[14,15,16],[17,18,19]])
#lface = Face.face([[21,22,23],[24,25,26],[27,28,29]])
#fface = Face.face([[31,32,33],[34,35,36],[37,38,39]])
#rface = Face.face([[41,42,43],[44,45,46],[47,48,49]])
#bface = Face.face([[51,52,53],[54,55,56],[57,58,59]])
#dface = Face.face([[61,62,63],[64,65,66],[67,68,69]])
mycube = cube.cube(uface,lface,fface,rface,bface,dface)

mysolver = solver.solver(mycube,"")
mysolver.solve()
mycube.showcube()